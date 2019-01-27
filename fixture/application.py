from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture_contact.contact import ContactHelper


class Application:

    def __init__(self, browser, base_url):
#        self.wd = WebDriver()
#        self.wd.implicitly_wait(5)
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "opera":
            self.wd = webdriver.Opera()
        else:
            raise ValueError("Unrecognized browser %s " % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url=base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)
#        wd.get("http://localhost:8080/addressbook/index.php")


    def destroy(self):
        self.wd.quit( )

