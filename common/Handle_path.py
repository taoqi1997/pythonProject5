import os
# 主目录
HOST_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 测试用例目录
TEST_DATA = os.path.join(HOST_PATH,"data")
# 配置文件路径
CONFIG = os.path.join(HOST_PATH,"conf")
# 日志文路径
LOG = os.path.join(HOST_PATH,"logs")
# 测试用例类的理路径
TEST_CASE = os.path.join(HOST_PATH,"test_case")
pass