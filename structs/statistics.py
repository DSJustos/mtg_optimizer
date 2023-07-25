import numpy as np
import seaborn as sns
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

class Statistics:
    def __init__(self, ):
        self.mulligan_count = []
        self.mulligan_results = []
        self.mulligan_keeps_dumps = []
        self.turn_logs = []
        self.game_df = None

    def __get_game_df(self):
        self.game_df = pd.DataFrame.from_records(data=self.turn_logs)
        self.game_df["counters_in_hand"] = self.game_df["hand"].apply(lambda x: x["counter"])
        self.game_df = self.game_df.drop(columns="hand").groupby(by=["turn_count"], as_index=False).mean()

    def __mulligan_success_hist(self):
        data = Counter(self.mulligan_count)
        data = pd.DataFrame(data=data.values(), index=data.keys(), columns=["probability"])
        data = data.reset_index()
        data = data.rename(columns={"index": "mulligans_to_success"})
        data["probability"] = data["probability"]/data["probability"].sum()
        data["mulligans_to_success"] = data["mulligans_to_success"].astype(str)
        data = data.sort_values(by="mulligans_to_success")

        fig = sns.barplot(data=data, x="mulligans_to_success", y="probability")
        fig.set(title="Number of mulligans until success")
        fig.get_figure().savefig("viz/mulligan_success_dist.png")

    def __per_turn_means_histograms(self):
        for col in self.game_df.drop(columns="turn_count").columns:
            self.__save_histogram_to_file(df=self.game_df, x="turn_count", y=col,
                                          title=f"Mean {col} per turn", file_name=f"viz/{col}_hist.png")

    def __save_histogram_to_file(self, df, x, y, title, file_name):
        fig = sns.barplot(data=df, x=x, y=y)
        fig.set(title=title)
        fig.get_figure().savefig(file_name)
        plt.clf()

    def finalize(self):
        self.__get_game_df()
        self.__mulligan_success_hist()
        self.__per_turn_means_histograms()


    def __str__(self):
        report = "REPORT"
        report += f"\nChance of mulligan success: {round(100*np.sum([i=='Success' for i in self.mulligan_results])/len(self.mulligan_count),2)}% "
        report += f"\nMulligans until success (mean): {round(np.mean(self.mulligan_count),2)}"
        return report
