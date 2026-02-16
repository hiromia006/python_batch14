class TestCase2:
    # Class variable (shared)
    test_type = "Regression"

    # Constructor
    def __init__(self, name, environment):
        # Instance variables
        self.test_name = name
        self.env = environment

    # Method
    def run_test(self):
        print("Test Type:", TestCase2.test_type)
        print("Running Test:", self.test_name)
        print("Environment:", self.env)

# Create instances of TestCase2
test1 = TestCase2("Login Test", "Staging")
print(test1.test_type)
test1.run_test()

test2 = TestCase2("Checkout Test", "Production")
print(test2.test_type)
test2.run_test()