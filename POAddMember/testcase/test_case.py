from POAddMember.page.main import Main


class TestPO:
    def setup(self):
        self.main = Main()

    def test_add_member(self):
        addmember = self.main.goto_add_member()
        addmember.add_member()
        # sleep(2)# ----在get_member()方法中添加显式等待逻辑
        assert "kongtianlong" in str(addmember.get_member())

        # self.main.goto_phone().add_member()



