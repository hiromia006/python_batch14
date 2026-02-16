class AssertionHelper:
    def varify_true(self, condition):
        if condition:
            print("Assertion Passed")
        else:
            print("Assertion Failed")

hp=AssertionHelper()
hp.varify_true(True)