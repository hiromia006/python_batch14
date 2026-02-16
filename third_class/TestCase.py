class TestCase:
    def __init__(self, test_name):
        self.test_name = test_name

    def run_test(self):
        print("Running test Case:", self.test_name)


test1 = TestCase("Test Case 1")
test1.run_test()

login_test = TestCase("Login Test")
login_test.run_test()

checkout_test = TestCase("Checkout Test")
checkout_test.run_test()