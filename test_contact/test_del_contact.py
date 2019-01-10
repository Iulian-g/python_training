from model_contact.contact import Contact

def test_delete_contact(app):
    if app.contact.count == 0:
        app.contact.create_new_contact(Contact(firstname="Michel", middlename="Remi", lastname="Nostredame",
                                  nickname="alchemist", title="astrological consultant", company="Paranormal", address="France",
                                  home="Saint-Remy-de-Provence, ", mobile="06 23 12 45 54 ", work="Physician", fax="+61-01-123-4567 ", email="france@gmail.com",
                                  email2="nostric@gmail.com", email3="actor@gmail.com", homepage="Final years",bday="13", bmonth="July", byear="1979", aday="23", amonth="July", ayear="1963", address2="was a French",
                                  phone2="00-63-02-1234567", notes="legends about his life"))
    app.contact.delete_contact()

