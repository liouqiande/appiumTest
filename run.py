# -*- coding: utf-8 -*-
import sys
import os
import pytest
import subprocess
import logging
import pytest_rerunfailures

# 添加项目路径到pythonPATH
sys.path.append(os.path.dirname(sys.modules[__name__].__file__))

# 设置logging
fileHandler = logging.FileHandler(filename="logs/uiauto.log", encoding="utf-8")
logging.getLogger().setLevel(0)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
fileHandler.setFormatter(formatter)
logging.getLogger().addHandler(fileHandler)

if __name__ == "__main__":
    # 生成 allure 测试报告
    # 运行登陆测试用例
    # pytest.main(['-sq', '--alluredir', 'reports/testreport', 'testcase/test_login.py'])
    # 运行首页测试用例
    pytest.main(['-sq', '--alluredir', 'reports/testreport', 'testcase/test_home_page.py'])
    print(subprocess.getstatusoutput('allure generate --clean reports/testreport/ -o reports/testreport/html'))