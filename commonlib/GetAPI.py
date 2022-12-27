# -*- coding: UTF-8 -*-
# =============================================================
# @Author: Jemma
# @Project: UnittestFramework -> GetAPI.py
# @Date: 12/27/2022 5:51 PM
# @Software: PyCharm
# @Version: python 3.10
# =============================================================
import requests

def get_API_without_parameter(url, headers):
    response = requests.get(url=url, headers=headers)
    return response