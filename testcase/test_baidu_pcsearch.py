import unittest
import json
from Constant import HEADERS
import commonlib.PostAPI as PostAPI
import commonlib.BasicReport as BasicReport
from ddt import ddt, data, unpack, file_data

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.url = r'https://ug.baidu.com/mcp/pc/pcsearch'


    def test_0010_post_pcsearch_with_json_check_errmsg(self):
        headers = {
            'User-Agent': HEADERS.UserAgent,
            'Content-Type': HEADERS.ContentTypeJson
        }
        data = {"invoke_info":{"pos_1":[{}],"pos_2":[{}],"pos_3":[{}]}}
        response = PostAPI.post_API_with_json(self.url, headers=headers, json=data)
        data = json.loads(response.text)
        print(response.text)
        self.assertEqual(response.status_code, 200, msg=f'response.status_code={response.status_code}，not 200')  # add assertion here
        self.assertEqual(data['errmsg'], 'ok', msg=f"errmsg={data['errmsg']}, not 'ok'")

    @file_data(r'D:\work\APIAutomation\TestData\PCSearch.json')
    def test_0020_post_pcsearch_with_json_check_action_rule(self, input, output):
        headers = {
            'User-Agent': HEADERS.UserAgent,
            'Content-Type': HEADERS.ContentTypeJson
        }
        response = PostAPI.post_API_with_json(self.url, headers=headers, json=input)
        data = json.loads(response.text)
        print(response.text)
        self.assertEqual(response.status_code, 200,
                         msg=f'response.status_code={response.status_code}，not 200')  # add assertion here
        self.assertEqual(data['data']['action_rule'], output['data']['action_rule'],
                         msg=f" actual action_rule={data['data']['action_rule']}\nexpect action_rule={output['data']['action_rule']}")


if __name__ == '__main__':
    suite = unittest.TestLoader().discover(r"./", "test_baidu_pcsearch.py")
    BasicReport.GenerateHtmlReport(
        description=r'Test Case for Baidu PCsearch',
        tester=r'Jemma',
        testlist=suite,
        title='API Test Report',
        language='en',
        verbosity=2,
        cleanLog=True)
