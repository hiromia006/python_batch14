class Browser:
    def start(self):
        print("Browser started")


class Chrome(Browser):
    def start(self):
        print("Chrome started")


class Firefox(Browser):
    def start(self):
        print("Firefox started")


ch = Chrome()
ch.start()

ff = Firefox()
ff.start()
