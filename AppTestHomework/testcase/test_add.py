import pytest

from AppTestHomework.page.app import App


class TestAdd:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    # @pytest.mark.parametrize('name, gender, number', [
    #     ('小小的', '女', '18679765432'),
    #     ('大大的', '男', '18679765434'),
    #     ('静静呀', '女', '18679765433')
    # ])
    # def test_addmember(self, name, gender, number):
    #     add = self.main.goto_list().addmember().edit().editinfo(name, gender, number)
    #
    #     assert '成功' in add.get_toast()

    def test_deletemember(self):
        self.main.goto_list().manage_contacts().deletemember()
