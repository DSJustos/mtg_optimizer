import numpy as np
import seaborn as sns
from collections import Counter
import pandas as pd

class Statistics:
    def __init__(self, ):
        self.mulligan_count = []

    def __mulligan_success_hist(self):
        data = ['fail' if x is np.nan else x for x in self.mulligan_count]
        data = Counter(data)
        data = pd.DataFrame(data=data.values(), index=data.keys(), columns=["probability"])
        data = data.reset_index()
        data = data.rename(columns={"index": "mulligans_to_success"})
        data["probability"] = data["probability"]/data["probability"].sum()
        data["mulligans_to_success"] = data["mulligans_to_success"].astype(str)
        data = data.sort_values(by="mulligans_to_success")

        fig = sns.barplot(data=data, x="mulligans_to_success", y="probability")
        fig.set(title="Number of mulligans until success")
        fig.get_figure().savefig("viz/mulligan_success_dist.png")

    def finalize(self):
        self.__mulligan_success_hist()

    def __str__(self):
        report = "REPORT"
        report += f"\nChance of mulligan success: {round(100*np.sum(~np.isnan(self.mulligan_count))/len(self.mulligan_count),2)}%"
        report += f"\nMulligans until success (mean): {round(np.nanmean(self.mulligan_count),2)}"
        return report
