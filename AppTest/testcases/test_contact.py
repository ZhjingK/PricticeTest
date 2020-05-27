from AppTest.page.app import App


class TestContact:
    def setup(self):
        # 继承的父类__init__()方法参数如果有默认值，在后续实例化的时候就不用填写参数
        self.app = App()
        self.main = self.app.start().main()

    def test_addcontact(self):
        invite = self.main.goto_addresslist().add_member().addmember_by_manul().input_name().set_gender().input_phone().click_post().click_save()
        assert '成功' in invite.get_toast()

