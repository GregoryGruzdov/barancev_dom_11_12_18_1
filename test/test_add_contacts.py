# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact(firstname="123", lastname="123", middlename="123", address2="123", email="email.email@email.com"))