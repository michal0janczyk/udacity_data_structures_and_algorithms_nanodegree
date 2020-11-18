#! usr/bin/env python3


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    @classmethod
    def is_user_in_group(self, user, group):
        """
        Return True if user is in the group, False otherwise.

        Arguments:
            user {[str]} - - [user name/id]
            group {[class:Group]} - - [group to check user membership against]

        Returns:
            [str] -- [description]
        """
        if user in group.get_users():
            return True
        else:
            if len(group.get_groups()) == 0:
                return False
            else:
                for sub_group in group.get_groups():
                    found = self.is_user_in_group(user, sub_group)
                    if found:
                        return True
        return False


def main():

    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(Group.is_user_in_group("parent", parent))
    parent_in = "parent"
    parent.add_user(parent_in)
    print(Group.is_user_in_group("parent", parent))
    print(Group.is_user_in_group("child", parent))
    print(Group.is_user_in_group("sub_child_user", parent))
    print(Group.is_user_in_group("", parent))
    print(Group.is_user_in_group("", child))


if __name__ == "__main__":
    main()
