class TestStatus:

    def passed(self):
        print("Test Passed")

    def failed(self):
        print("Test Failed")


st = TestStatus()
st.passed()
st.failed()

from Encapsulation import Credentials
cred = Credentials()
print(cred.get_password())