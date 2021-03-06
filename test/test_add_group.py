# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(groupname="123", groupheader="123", groupfooter="123"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(groupname="", groupheader="", groupfooter=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
