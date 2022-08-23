import logging
import os
from common.Handle_path import LOG
def Handle_log(name="taoqi",log_level="DEBUG",fh_name = "taoqi_01log",fh_level = "DEBUG",sh_name="taoqi"):
    # 创建日志收集器
    log = logging.getLogger(name)
    # 设置日志手机等级
    log.setLevel(log_level)
    # 创建输出平台，输出到文件
    fh = logging.FileHandler(fh_name,encoding="utf-8")
    fh.setLevel(fh_level)
    log.addHandler(fh)
    # 输出到控制台
    sh = logging.StreamHandler(sh_name)
    sh.setLevel("DEBUG")
    log.addHandler(sh)
    #创建日志输出格式
    format = "%(asctime)s-%(filename)s-%(lineno)d--%(levelname)s-%(message)s"
    # 设置收集器格式
    log_format = logging.Formatter(format)
    # 为输出渠道绑定输出格式
    fh.setFormatter(log_format)
    sh.setFormatter(log_format)
    return log
my_log = Handle_log(fh_name=os.path.join(LOG,"my_log"))


