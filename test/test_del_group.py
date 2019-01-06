from model.group import Group


def test_delete_first_group_py(app):
    if app.group.count == 0:
        app.group.create(Group(name="test"))
    old_group = app.group.get_group_list( )
    app.group.delete_first_group()
    new_group = app.group.get_group_list( )
    assert len(old_group) - 1 == len(new_group)

