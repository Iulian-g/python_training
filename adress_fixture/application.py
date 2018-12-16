from selenium.webdriver.firefox.webdriver import WebDriver
from adress_fixture.session import SessionHelper
from adress_fixture.contact import ContactHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
            # open home page
            wd = self.wd
            wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()