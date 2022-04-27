from pathlib import Path

import cv2
import imutils
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity

"""
Usage:

image_1_path = r'.\gf1vip_8542.png'
image_2_path = r'.\gf1vip_8542 - 複製.png'
diff_path = r'.\gf1vip_8542_result'
name = 'gf1vip_8542'
result = MarkDiffImg().mark_diff_img(
    base_png=image_1_path,
    running_png=image_2_path,
    diff_dir= diff_path,
    name=name
    )

print(result)
"""


class MarkDiffImg:
    @staticmethod
    def cv_imread(file_path):
        """
        讀取圖片（解決路徑中含有中文無法讀取的問題），一般是直接cv2.imread(filea_path)
        :param file_path:圖片的路徑
        :return:
        """
        cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
        return cv_img

    @classmethod
    def mark_diff_img(cls, base_png: str, running_png: str, diff_dir: str, name: str):
        """
        對比圖片並標出差異，保存差異圖片
        """
        result = cls.Result()

        # 加載兩張圖片並將他們轉換為灰度
        image_a = cls.cv_imread(base_png)
        image_b = cls.cv_imread(running_png)
        gray_a = cv2.cvtColor(image_a, cv2.COLOR_BGR2GRAY)
        gray_b = cv2.cvtColor(image_b, cv2.COLOR_BGR2GRAY)

        # 計算兩個灰度圖像之間的結構相似度指數
        (score, diff) = structural_similarity(gray_a, gray_b, full=True)
        diff = (diff * 255).astype("uint8")
        print("SSIM:{}".format(score))

        # 找到不同點的輪廓以致於我們可以在被標識為“不同”的區域周圍放置矩形
        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # 找到一系列區域，在區域周圍放置矩形
        for c in cnts:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(image_a, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.rectangle(image_b, (x, y), (x + w, y + h), (255, 0, 0), 2)

        if len(cnts) != 0:
            diff_dir = Path(diff_dir)
            if not diff_dir.exists():
                diff_dir.mkdir(parents=True)

            # 基礎截圖標出與運行時截圖的差異 圖片
            diff_base_png = str(diff_dir / (name + "_base.png"))
            # 運行時截圖標出與基礎截圖的差異 圖片
            diff_running_png = str(diff_dir / (name + "_running.png"))
            # 保存差異圖片
            cv2.imencode(".jpg", image_a)[1].tofile(diff_base_png)
            cv2.imencode(".jpg", image_b)[1].tofile(diff_running_png)
            # 水平結合兩張圖 (base(沒畫圈的) 和 running(有畫圈的))
            concat_png = str(diff_dir / (name + "_result.png"))
            cls.get_concat_h(Image.open(base_png), Image.open(diff_running_png)).save(concat_png)

            result.base_path = diff_base_png
            result.running_path = diff_running_png
            result.result_path = concat_png
            result.diff_count = len(cnts)
            result.is_diff = True

        return result

    @staticmethod
    def get_concat_h(im1, im2):
        # 水平串接圖片
        dst = Image.new("RGB", (im1.width + im2.width, im1.height))
        dst.paste(im1, (0, 0))
        dst.paste(im2, (im1.width, 0))
        return dst

    @staticmethod
    def get_concat_v(im1, im2):
        # 垂直串接圖片
        dst = Image.new("RGB", (im1.width, im1.height + im2.height))
        dst.paste(im1, (0, 0))
        dst.paste(im2, (0, im1.height))
        return dst

    class Result:
        def __init__(
            self,
            base_path=None,
            running_path=None,
            result_path=None,
            diff_count=0,
            is_diff=False,
        ):
            self.base_path = base_path
            self.running_path = running_path
            self.result_path = result_path
            self.diff_count = diff_count
            self.is_diff = is_diff
