from model_contact.contact import Contact
from random import randrange

def test_modify_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="Michel", middlename="Remi", lastname="Nostredame",
                                  nickname="alchemist", title="astrological consultant", company="Paranormal", address="France",
                                  home="Saint-Remy-de-Provence, ", mobile="06 23 12 45 54 ", work="Physician", fax="+61-01-123-4567 ", email="france@gmail.com",
                                  email2="nostric@gmail.com", email3="actor@gmail.com", homepage="Final years",bday="13", bmonth="July", byear="1979", aday="23", amonth="July", ayear="1963", address2="was a French",
                                  phone2="00-63-02-1234567", notes="legends about his life")
    contact = Contact(firstname="Ivan", lastname="Ivanov")
    index = randrange(len(old_contact))
    if app.contact.count() == 0:
        app.contact.create_new_contact(contact)
    contact.id = old_contact[index].id
    app.contact.modify_contact_by_index(contact,index)
    old_contact[index] = contact
    assert len(old_contact) == app.contact.count()
    new_contact = app.contact.get_contact_list()
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

#    app.contact.modify_contact(Contact(firstname="New", middlename="Year", lastname="2019",
#                                 nickname="God", title="Consultant", company="Normal", address="Italy",
#                                  home="Provence, ", mobile="09 23 12 45 54 ", work="IT", fax="+99-01-123-4567 ", email="franco@gmail.com",
#                                  email2="nos@gmail.com", email3="or@gmail.com", homepage="New years", bday="14", bmonth="July", byear="1963", aday="18", amonth="July", ayear="1990", address2="was",
#                                  phone2="11-63-02-1234567", notes="legends life"))


