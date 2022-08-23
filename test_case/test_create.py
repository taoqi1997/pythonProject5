import unittest
import requests
import os
import random
from unittestreport import ddt,list_data
from common.handle_conf import conf
from common.handle_excel import Handle_excel
from common.Handle_path import TEST_DATA
from test_case.dict_assert import dict_assert
from common.Handle_log import my_log
from jsonpath import jsonpath
from common.handlr_data import handle_data

@ddt
class Test_create(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        # 获取token
        url = eval(conf.get("URL","url"))+"/cgi-bin/token"
        params ={"grant_type":"client_credential",
                 "appid":"wx871c3c2b650e51b0",
                 "secret":"4c278d92b86614a6c832e687936a5435"}
        response = requests.get(url=url,params=params)
        res = response.json()
        print(res)
        cls.token = jsonpath(res,"$.access_token")
        print(cls.token)

    def random_name(self):
        name_id = random.randint(1400,2000)
        return name_id

    excel = Handle_excel(os.path.join(TEST_DATA, "test_data.xlsx"), "create")
    cases = excel.Read_excel()
    @list_data(cases)
    def test_creat(self,item):
        # 准备测试数据
        url = eval(conf.get("URL","url"))+item["url"]
        method = item["method"]
        params = {"access_token":self.token}
        # 随机生成标签
        # 参数
        name_id =self.random_name()
        data =item["data"].replace("#name_id#",str(name_id))
        json = eval(data)
        # 预期结果
        exp = item["expected"].replace("#name_id#",str(name_id))
        expect = eval(exp)
        # 调用接口
        response = requests.request(url=url,method=method,params=params,json=json)
        res = response.json()
        print(expect)
        print(res)
        # 断言
        try:
            dict_assert(expect=expect,res=res)
        except AssertionError as e:
            my_log.error("用例-----{}-----执行失败".format(item["title"]))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例-----{}-----执行成功".format(item["title"]))







