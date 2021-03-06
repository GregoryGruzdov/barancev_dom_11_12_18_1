# -*- coding: utf-8 -*-


def test_delete_first_group(app):
    app.group.prepare_groups()
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
