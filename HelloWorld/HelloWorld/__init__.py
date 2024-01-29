# 在与 settings.py 同级目录下的 __init__.py 中引入模块和进行配置
import sys
sys.path.insert(0,"/Library/Python/3.9/site-packages")
import pymysql

pymysql.install_as_MySQLdb()
