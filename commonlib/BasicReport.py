# -*- coding: UTF-8 -*-
# =============================================================
# @Author: Jemma
# @Project: UnittestFramework -> BasicReport.py
# @Date: 12/27/2022 5:50 PM
# @Software: PyCharm
# @Version: python 3.10
# =============================================================
import os
import datetime
import unittest
from XTestRunner import HTMLTestRunner
from Constant import FILEPATH

def GenerateHtmlReport(
        description,
        tester,
        testlist,
        title='API Test Report',
        language='en',
        verbosity=2,
        cleanLog=True):
    pathName = FILEPATH.ReportPath
    if not os.path.exists(pathName):
        os.mkdir(pathName)

    if cleanLog:
        for file in os.listdir(pathName):
            if file.endswith(".html") or file.endswith(".png") or file.endswith(".log"):
                pathFile = os.path.join(pathName, file)
                os.remove(pathFile)

    reportPath = datetime.datetime.strftime(datetime.datetime.now(
    ), "%Y%m%d%H%M%S") + "_{0}_Result.html".format(description.replace(" ", ""))

    with(open('{0}/{1}'.format(pathName, reportPath), 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title=title,
            description=description,
            tester=tester,
            language=language,
            verbosity=verbosity,
        )
        runner.run(
            testlist=testlist,
            rerun=0,
            save_last_run=False
        )
        fp.close()


def GenerateTxtReport(description, testList, verbosity=1, cleanLog=True):
    pathName = FILEPATH.ReportPath
    if not os.path.exists(pathName):
        os.mkdir(pathName)

    if cleanLog:
        for f in os.listdir(pathName):
            if f.endswith(".html") or f.endswith(".png") or f.endswith(".log"):
                pathFile = os.path.join(pathName, f)
                os.remove(pathFile)

    reportPath = datetime.datetime.strftime(datetime.datetime.now(
    ), "%Y%m%d%H%M%S") + "_{0}_Result.log".format(description.replace(" ", ""))

    with(open('{0}/{1}'.format(pathName, reportPath), 'a')) as fp:
        runner = unittest.TextTestRunner(stream=fp, verbosity=verbosity)
        print(runner.run(testList))
        fp.close()
