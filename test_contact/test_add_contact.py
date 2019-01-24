# -*- coding: utf-8 -*-

from model_contact.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", homephone="", mobilephone="", workphone="", fax="",
                                  email="", email2="", email3="",homepage="", address2="",
                                  secondaryphone="", notes="")] + [
     Contact(firstname=random_string("firstname", 20), middlename=random_string("middlename", 20), lastname=random_string("lastname", 20),
             nickname=random_string("nickname", 20), title=random_string("title", 20), company=random_string("company", 20),
             address=random_string("address", 20),
             homephone=random_string("homephone", 20), mobilephone=random_string("mobilephone", 20), workphone=random_string("workphone", 20),
             fax=random_string("fax", 20), email=random_string("email", 20),
             email2=random_string("email2", 20), email3=random_string("email3", 20), homepage=random_string("homepage", 20),
             secondaryphone=random_string("secondaryphone", 20), notes=random_string("notes", 20))
     for i in range (5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contact = app.contact.get_contact_list( )
    app.contact.create_new_contact(contact)
    assert len(old_contact)+1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


#             bday=random_string("5", 20), bmonth=random_string("October", 20), byear=random_string("1965", 20), aday=random_string("27", 20),
#             amonth=random_string("May", 20), ayear=random_string("1989", 20), address2=random_string("address2", 20),
#bday="", bmonth="", byear="", aday="", amonth="", ayear="",