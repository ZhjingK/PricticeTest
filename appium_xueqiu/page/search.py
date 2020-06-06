from appium_xueqiu.page.base_page import BasePage


class Search(BasePage):
    def search(self, name):
        # 给_parame赋值，便于进行
        self._parame['name'] = name
        self.steps('../page/search.yaml')

    def add(self, name):
        self._parame['name'] = name
        self.steps('../page/search.yaml')

    def is_add(self, name):
        self._parame['name'] = name
        return self.steps('../page/search.yaml')

    def reset(self, name):
        self._parame['name'] = name
        return self.steps('../page/search.yaml')

