import pytest
import yaml

from appium_xueqiu.page.app import App


class TestSearch():
    def setup(self):
        self.search = App().start().main().goto_market().goto_search()

    # 对参数进行数据驱动
    @pytest.mark.parametrize('name', yaml.safe_load(open("./test_case.yaml", encoding='utf-8')))
    def test_search(self, name):
        self.search.search(name)
        if self.search.is_add(name):
            self.search.reset(name)
        self.search.add(name)

        assert self.search.is_add(name)

