import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator


class GraphDrawer:
    def __init__(self):
        pass

    def draw(
        self,
        y_pass,
        y_fail,
        y_error,
        title,
        xlabel,
        ylabel,
        tick_labels,
        bar_width=0.2,
        tick_alpha=0.5,
        filepath=None,
    ):
        """
        file name extension can be pdf or png
        """
        if len(y_pass) != len(y_fail) or len(y_fail) != len(y_error) or len(y_pass) != len(y_error):
            raise Exception("length of pass, fail, error should be equal")

        size = len(y_pass)
        x_month = np.arange(size)

        plt.title(title)  # 圖表標題
        plt.xlabel(xlabel)  # x軸標題
        plt.ylabel(ylabel)  # y軸標題
        plt.xticks(x_month + bar_width / 2, tick_labels, fontsize=5, rotation=60)  # 畫上tick label

        bar_pass = plt.bar(
            x_month,
            y_pass,
            align="center",
            color="green",
            width=bar_width,
            label="Pass",
            alpha=tick_alpha,
        )
        bar_fail = plt.bar(
            x_month + bar_width,
            y_fail,
            align="center",
            color="red",
            width=bar_width,
            label="Fail",
            alpha=tick_alpha,
        )
        bar_error = plt.bar(
            x_month + 2 * bar_width,
            y_error,
            align="center",
            color="yellow",
            width=bar_width,
            label="Error",
            alpha=tick_alpha,
        )

        self._createLabels(bar_pass)
        self._createLabels(bar_fail)
        self._createLabels(bar_error)
        ax = plt.gca()
        ax.yaxis.set_major_locator(MultipleLocator(1))
        plt.ylim(0, 10)

        plt.legend()  # 右上圖示說明

        if filepath:
            plt.savefig(filepath, bbox_inches="tight", pad_inches=0.0)

        plt.show()

    @staticmethod
    def _createLabels(data):
        # 使得每個長條圖上顯示資料標籤，詳見：[https://stackoverflow.com/questions/40489821/how-to-write-text-above-the-bars-on-a-bar-plot-python]
        for item in data:
            height = item.get_height()
            plt.text(
                item.get_x() + item.get_width() / 2.0,
                height * 1.05,
                "%d" % int(height),
                ha="center",
                va="bottom",
                fontsize=5,
            )
