# -*- coding: utf-8 -*-

from model_contact.contact import Contact

def test_add_contact(app):
    old_contact = app.contact.get_contact_list( )
    contact = Contact(firstname="Michel", middlename="Remi", lastname="Nostredame",
                                  nickname="alchemist", title="astrological consultant", company="Paranormal", address="France",
                                  home="Saint-Remy-de-Provence, ", mobile="06 23 12 45 54 ", work="Physician", fax="+61-01-123-4567 ", email="france@gmail.com",
                                  email2="nostric@gmail.com", email3="actor@gmail.com", homepage="Final years",bday="13", bmonth="July", byear="1979", aday="23", amonth="July", ayear="1963", address2="was a French",
                                  phone2="00-63-02-1234567", notes="legends about his life")
    app.contact.create_new_contact(contact)
    assert len(old_contact)+1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#        app.contact.create_new_contact(Contact(firstname="", middlename="", lastname="",
#                                    nickname="", title="", company="", address="",
#                                    home="", mobile="", work="", fax="",
#                                    email="",
#                                    email2="", email3="", homepage="", bday="", bmonth="", byear="", aday="", amonth="", ayear="", address2="",
#                                    phone2="", notes=""))

