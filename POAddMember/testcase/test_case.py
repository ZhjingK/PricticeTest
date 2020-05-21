from POAddMember.page.main import Main


class TestPO:
    def setup(self):
        self.main = Main()

    def test_add_member(self):
        # addmember = self.main.goto_add_member()
        # addmember.add_member()
        # sleep(2)
        # assert "kongtianlong" in str(addmember.get_member())

        self.main.goto_phone().add_member()



