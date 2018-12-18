from selenium.webdriver.support.select import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
         # open and init form adress book
         wd = self.app.wd
         wd.find_element_by_link_text("add new").click()
         wd.find_element_by_name("firstname").click()
         wd.find_element_by_name("firstname").clear()
         wd.find_element_by_name("firstname").send_keys(contact.firstname)
         wd.find_element_by_name("middlename").click()
         wd.find_element_by_name("middlename").clear()
         wd.find_element_by_name("middlename").send_keys(contact.middlename)
         wd.find_element_by_name("lastname").click()
         wd.find_element_by_name("lastname").clear()
         wd.find_element_by_name("lastname").send_keys(contact.lastname)
         wd.find_element_by_name("nickname").click()
         wd.find_element_by_name("nickname").clear()
         wd.find_element_by_name("nickname").send_keys(contact.nickname)
         wd.find_element_by_name("title").click()
         wd.find_element_by_name("title").clear()
         wd.find_element_by_name("title").send_keys(contact.title)
         wd.find_element_by_name("company").click()
         wd.find_element_by_name("company").clear()
         wd.find_element_by_name("company").send_keys(contact.company)
         wd.find_element_by_name("address").click()
         wd.find_element_by_name("address").clear()
         wd.find_element_by_name("address").send_keys(contact.address)
         wd.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Address:'])[1]/following::label[1]").click()
         wd.find_element_by_name("home").click()
         wd.find_element_by_name("home").click()
         wd.find_element_by_name("home").clear()
         wd.find_element_by_name("home").send_keys(contact.home)
         wd.find_element_by_name("mobile").click()
         wd.find_element_by_name("mobile").clear()
         wd.find_element_by_name("mobile").send_keys(contact.mobile)
         wd.find_element_by_name("work").click()
         wd.find_element_by_name("work").clear()
         wd.find_element_by_name("work").send_keys(contact.work)
         wd.find_element_by_name("fax").click()
         wd.find_element_by_name("fax").send_keys(contact.fax)
         wd.find_element_by_name("email").click()
         wd.find_element_by_name("email").clear()
         wd.find_element_by_name("email").send_keys(contact.email)
         wd.find_element_by_name("email2").click()
         wd.find_element_by_name("email2").clear()
         wd.find_element_by_name("email2").send_keys(contact.email2)
         wd.find_element_by_name("email3").click()
         wd.find_element_by_name("email3").clear()
         wd.find_element_by_name("email3").send_keys(contact.email3)
         wd.find_element_by_name("homepage").click()
         wd.find_element_by_name("homepage").clear()
         wd.find_element_by_name("homepage").send_keys(contact.homepage)
         wd.find_element_by_name("bday").click()
         Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
         wd.find_element_by_name("bmonth").click()
         Select(wd.find_element_by_name("bmonth")).select_by_visible_text("February")
         wd.find_element_by_name("byear").click()
         wd.find_element_by_name("byear").clear()
         wd.find_element_by_name("byear").send_keys("1986")
         wd.find_element_by_name("aday").click()
         Select(wd.find_element_by_name("aday")).select_by_visible_text("3")
         wd.find_element_by_name("amonth").click()
         Select(wd.find_element_by_name("amonth")).select_by_visible_text("April")
         wd.find_element_by_name("ayear").click()
         wd.find_element_by_name("ayear").clear()
         wd.find_element_by_name("ayear").send_keys("1989")
         wd.find_element_by_name("address2").click()
         wd.find_element_by_name("address2").clear()
         wd.find_element_by_name("address2").send_keys(contact.address2)
         wd.find_element_by_name("theform").click()
         wd.find_element_by_name("phone2").click()
         wd.find_element_by_name("phone2").clear()
         wd.find_element_by_name("phone2").send_keys(contact.phone2)
         wd.find_element_by_name("notes").click()
         wd.find_element_by_name("notes").clear()
         wd.find_element_by_name("notes").send_keys(contact.notes)

    def delete_contact(self):
         wd = self.app.wd
         wd.find_element_by_name("selected[]").click()
         wd.find_element_by_xpath("//input[@value='Delete']").click( )
         # wd.find_element_by_name("Delete").click()
         wd.switch_to_alert().accept( )



