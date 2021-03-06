import allure
import pytest

from page.mis.mis_login_page import MisLoginProxy
from utils import DriverUtils, is_element_exist


# 定义测试类
@pytest.mark.run(order=102)
class TestMisLogin:
    # 定义类级别的初始化方法
    def setup_class(self):
        # 1.打开浏览器
        self.driver = DriverUtils.get_mis_driver()
        # 创建业务方法所在的类的对象
        self.mis_login_proxy = MisLoginProxy()

    # 定义测试方法
    def test_mis_login(self):
        # 2.定义测试数据
        username = "testid"
        password = "testpwd123"
        # 3.调用业务方法 --- >执行手工测试用例的操作步骤
        self.mis_login_proxy.test_mis_login(username, password)
        # 4.执行断言
        assert is_element_exist(self.driver, "退出")

    # 定义类级别的销毁方法
    # 5.关闭浏览器
    def teardown_class(self):
        DriverUtils.quit_mis_driver()
