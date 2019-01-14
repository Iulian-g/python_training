
from model_contact.contact import Contact
from random import randrange


def test_delete_contact(app):
    if app.contact.count == 0:
        app.contact.create_new_contact(Contact(firstname="test"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.delete_contact_by_index(index)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact)-1 == app.contact.count()
    old_contact[index:index+1] = []
    assert new_contact == old_contact