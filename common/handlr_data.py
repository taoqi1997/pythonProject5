import re
from  common.handle_conf import conf


def handle_data(cls,data):
    while re.search("#(.+?)#",data):
        res = re.search("#(.+?)#",data)
        res1 = res.group()
        attr = res.group(1)
        # 获取测试类中需要替换的数据
        try:
            value = getattr(cls,attr)
        except AttributeError:
            value = conf.get("test_data",attr)
        data = data.replace(res1,str(value))
    return data


#
# if __name__ == '__main__':
#     data = "datadasa3j#dkada#skldkhasd"
#     a = handle_data(data=data)
#     print(a)