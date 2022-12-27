import unittest
from Constant import HEADERS
import commonlib.BasicReport
from commonlib.GetAPI import get_API_without_parameter
from commonlib.PostAPI import post_API_without_parameter


class BaiduCase(unittest.TestCase):

    def setUp(self) :
        self.url = r'https://www.baidu.com/s'

    def test_0010_get_baidu(self):
        headers = {
            'User-Agent': HEADERS.UserAgent,
            'Content-Type': HEADERS.ContentTypeJson
        }
        response = get_API_without_parameter(self.url, headers=headers)
        self.assertEqual(response.status_code, 200, msg=f"actual status code:{response.status_code}, not 200")  # add assertion here

    def test_0020_post_baidu(self):
        headers = {
            'User-Agent': HEADERS.UserAgent,
            'Content-Type': HEADERS.ContentTypeJson
        }
        response = post_API_without_parameter(self.url, headers=headers)
        self.assertEqual(response.status_code, 300,
                         msg=f"actual status code:{response.status_code}, not 300")  # add assertion here

    @unittest.skip("Not need to test this case after 12/27")
    def test_0030_skip_baidu(self):
        headers = {
            'User-Agent': HEADERS.UserAgent,
            'Content-Type': HEADERS.ContentTypeJson
        }
        response = get_API_without_parameter(self.url, headers=headers)
        self.assertEqual(response.status_code, 300,
                         msg=f"actual status code:{response.status_code}, not 300")  # add assertion here


if __name__ == '__main__':
    suite = unittest.TestLoader().discover(r"./", "test_baidu.py")
    commonlib.BasicReport.GenerateHtmlReport(
        description=r'Test Case for Baidu',
        tester=r'Jemma',
        testlist=suite,
        title='API Test Report',
        language='en',
        verbosity=2,
        cleanLog=True)