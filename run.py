import sys

sys.path.append("..")

import unittest
from unittestreport import TestRunner
from common.Handle_path import TEST_CASE

test = unittest.defaultTestLoader.discover(TEST_CASE)
runner = TestRunner(test,title="接口测试报告",tester="taoqi")
runner.run()