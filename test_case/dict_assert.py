# 判断预期结果是否在实际结果中

def dict_assert(expect,res):
    # 遍历预期结果
    for key,value in expect.items():
        if res.get(key) == value:
            pass
        else:
            raise AssertionError("{}不在{}里面".format(expect,res))