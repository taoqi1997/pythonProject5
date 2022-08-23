import unittest
import os
import requests
from unittestreport import ddt, list_data
from common.handle_excel import Handle_excel
from common.Handle_path import TEST_DATA
from common.handle_conf import conf
from common.Handle_log import my_log
from test_case.dict_assert import dict_assert

@ddt
class Handle_test(unittest.TestCase):
    workbook = Handle_excel(os.path.join(TEST_DATA,"test_data.xlsx"),"token")
    cases = workbook.Read_excel()

    @list_data(cases)
    def test_token(self,item):
        # 准备测试数据
        url = eval(conf.get("URL","url")) +item["url"]
        params = eval(item["data"])
        method = item["method"]
        expect = eval(item["expected"])
        #测试接口
        response = requests.request(url=url,params=params,method=method)
        res = response.json()
        print(expect)
        print(res)
        # 断言
        try:
            dict_assert(expect=expect,res=res)

        except AssertionError as e:
            my_log.error("用例---{}---执行未通过".format(item["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例---{}---执行通过".format(item["title"]))



