# -*- coding: UTF-8 -*-
# =============================================================
# @Author: Jemma
# @Project: UnittestFramework -> DealWithFile.py
# @Date: 12/27/2022 5:51 PM
# @Software: PyCharm
# @Version: python 3.10
# =============================================================
import csv
import os
import pyautogui
import base64
from Constant import FILEPATH


def get_screenshot(filename):
    if not os.path.exists(FILEPATH.ReportPath):
        os.mkdir(FILEPATH.ReportPath)
    screenshotpath = os.path.join(FILEPATH.ReportPath, filename)
    pyautogui.screenshot(screenshotpath)
    with open(screenshotpath, 'rb') as f:
        bytedata = f.read()
    base64file = base64.b64encode(bytedata).decode('ascii')
    return base64file


def get_txt_info(filepath):
    rows = []
    if filepath.endswith(".txt"):
        with open(filepath, 'rt') as f:
            readers = csv.reader(f, delimiter=",", quotechar="|")
            for row in readers:
                col = []
                for data in row:
                    col.append(data)
                rows.append(col)
        return rows
    else:
        return