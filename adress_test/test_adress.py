# -*- coding: utf-8 -*-

from adress_model.contact import Contact


def test_adress_py(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(firstname="gfhg", middlename="gfhf", lastname="fghfgh",
                                  nickname="fghfgh", title="fghfgh", company="fghfgh", address="fghfgh",
                                  home="fghfgh", mobile="fghfgh", work="fghfgh", fax="fghfgh", email="fghfgh",
                                  email2="fghfg", email3="fghfgh", homepage="fghfgh", address2="fghfg",
                                  phone2="fghfgh", notes="fghfgh"))
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
