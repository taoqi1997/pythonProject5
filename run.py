import sys
import os
from common.Handle_path import HOST_PATH
sys.path.append(os.path.join(HOST_PATH,"run.py"))
import unittest
from unittestreport import TestRunner
from common.Handle_path import TEST_CASE



test = unittest.defaultTestLoader.discover(TEST_CASE)
runner = TestRunner(test,title="接口测试报告",tester="taoqi")
runner.run()