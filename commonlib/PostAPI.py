# -*- coding: UTF-8 -*-
# =============================================================
# @Author: Jemma
# @Project: UnittestFramework -> PostAPI.py
# @Date: 12/27/2022 5:52 PM
# @Software: PyCharm
# @Version: python 3.10
# =============================================================
import requests

def post_API_without_parameter(url, headers):
    response = requests.post(url=url, headers=headers)
    return response

def post_API_with_json(url, headers, json):
    response = requests.post(url=url, headers=headers, json=json)
    return response