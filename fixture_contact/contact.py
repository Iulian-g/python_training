
from selenium.webdriver.support.select import Select
from model_contact.contact import Contact
import re



class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_contacts_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/") and len(wd.find_elements_by_name("to_group"))>0:
            return
        wd.find_element_by_link_text("home").click()

    def select_contact(self, index):
        # select first contact
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def change_field_file(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).send_keys(text)


    def change_field_select(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_contact(self, contact):
        wd = self.app.wd
        self.change_field("firstname", contact.firstname)
        self.change_field("middlename", contact.middlename)
        self.change_field("lastname", contact.lastname)
        self.change_field("nickname", contact.nickname)
        self.change_field("title", contact.title)
        self.change_field("company", contact.company)
        self.change_field("address", contact.address)
        self.change_field("home", contact.home)
        self.change_field("mobile", contact.mobile)
        self.change_field("work", contact.work)
        self.change_field("fax", contact.fax)
        self.change_field("email", contact.email)
        self.change_field("email2", contact.email2)
        self.change_field("email3", contact.email3)
        self.change_field("homepage", contact.homepage)
        self.change_field_select("bday", contact.bday)
        self.change_field_select("bmonth", contact.bmonth)
        self.change_field("byear", contact.byear)
        self.change_field_select("aday", contact.bday)
        self.change_field_select("amonth", contact.bmonth)
        self.change_field("ayear", contact.byear)
        self.change_field("address2", contact.address2)
        self.change_field("phone2", contact.phone2)
        self.change_field("notes", contact.notes)

    def create_new_contact(self, contact):
        wd = self.app.wd
        self.return_to_contacts_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contacts_cash = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        # delete contact
        wd = self.app.wd
        self.return_to_contacts_page()
        self.select_contact(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
#        self.return_to_contacts_page()
        self.contacts_cash = None
        wd.find_elements_by_css_selector("div.msgbox")

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def modify_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.return_to_contacts_page()
        self.select_contact(index)
        #wd.find_elements_by_css_selector("img[alt=\"Edit\"]")[index].click()
        self.open_edit_page_by_index(index)
        self.fill_contact(contact)
        wd.find_element_by_name("update").click()
        self.contacts_cash = None

    def open_edit_page_by_index(self, index):
        wd = self.app.wd
        self.return_to_contacts_page( )
        wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click( )

    def open_view_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_contacts_page( )
        wd.find_elements_by_css_selector("[title='Details']")[index].click( )

#    def open_contact_to_edit_by_index(self, index):
#        wd = self.app.wd
#        self.return_to_contacts_page( )
#        row = wd.find_elements_by_name("entry")[index]
#        cell = row.find_elements_by_tag_name("td")[7]
#        cell.find_element_by_tag_name("a").click( )

#    def open_contact_view_by_index(self, index):
#        wd = self.app.wd
#        self.return_to_contacts_page( )
#        row = wd.find_elements_by_name("entry")[index]
#        cell = row.find_elements_by_tag_name("td")[6]
#        cell.find_element_by_tag_name("a").click( )


    def count(self):
        wd = self.app.wd
        self.return_to_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cash = None

    def get_contact_list(self):
        if self.contacts_cash is None:
            wd = self.app.wd
            self.return_to_contacts_page()
            self.contacts_cash = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                id = element.find_element_by_css_selector("td.center").find_element_by_name("selected[]").get_attribute("value")
                lastname = element.find_element_by_xpath(".//td[2]").text
                firstname = element.find_element_by_xpath(".//td[3]").text
                address = element.find_element_by_xpath(".//td[4]").text
                all_emails = element.find_element_by_xpath(".//td[5]").text
                all_phones = element.find_element_by_xpath(".//td[6]").text
                self.contacts_cash.append(Contact(lastname=lastname, firstname=firstname, address=address, id=id, all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contacts_cash)


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_edit_page_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, email=email, email2=email2, email3=email3, homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_view_contact_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)