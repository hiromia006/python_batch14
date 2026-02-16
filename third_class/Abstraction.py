from abc import ABC, abstractmethod


class Browser(ABC):
    @abstractmethod
    def start(self):
        pass


class Chrome(Browser):
    def start(self):
        print("Starting Chrome browser")
        print("Open Chrome browser")


class Firefox(Browser):
    def start(self):
        print("Starting Firefox browser")

ch= Chrome()
ch.start()
print("-----------------------------")
ff = Firefox()
ff.start()