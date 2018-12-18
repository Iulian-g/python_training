# -*- coding: utf-8 -*-

from adress_model.contact import Contact


def test_adress_py(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(firstname="Michel", middlename="Remi", lastname="Nostredame",
                                  nickname="alchemist", title="astrological consultant", company="Paranormal", address="France",
                                  home="Saint-Remy-de-Provence, ", mobile="06 23 12 45 54 ", work="Physician", fax="+61-01-123-4567 ", email="france@gmail.com",
                                  email2="nostric@gmail.com", email3="actor@gmail.com", homepage="Final years", address2="was a French",
                                  phone2="00-63-02-1234567", notes="legends about his life"))
        app.session.logout()

def test_adress_empty_py(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(firstname="", middlename="", lastname="",
                                     nickname="", title="", company="", address="",
                                     home="", mobile="", work="", fax="",
                                     email="",
                                     email2="", email3="", homepage="", address2="",
                                     phone2="", notes=""))
        app.session.logout()
