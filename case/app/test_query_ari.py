import unittest

from parameterized import parameterized

from page.app.index_page import IndexProxy
from utils import DriverUtils, is_el_by_attribute


class TestQyAritcal(unittest.TestCase):
    # 3.定义初始化方法
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtils.get_app_driver()
        cls.index_proxy = IndexProxy()

    def setUp(self):
        self.driver.start_activity("com.itcast.toutiaoApp", ".MainActivity")
        # 4.定义测试方法

    @parameterized.expand(["架构", "linux"])
    def test_qy_aritcal(self, channel_name):
        # i鸱用根据频道查询文章的业务方法
        self.index_proxy.test_qari_by_channel(channel_name)
        # 断言
        self.assertTrue(is_el_by_attribute(self.driver, "text", "点赞"))

    @classmethod
    def tearDownClass(cls):
        DriverUtils.quit_app_driver()
