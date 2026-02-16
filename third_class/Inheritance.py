class BaseTest:
    def setup(self):
        print("Browser setup")


class Login(BaseTest):
    def test_login(self):
        print("Login test executed")


lg = Login()
lg.setup()
lg.test_login()
