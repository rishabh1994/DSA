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


def isUserInGroup(userName, group):
    answer = False
    if userName and group:
        if userName in group.get_users():
            answer = answer | True
        elif group.get_groups():
            for subGroup in group.get_groups():
                answer = answer | isUserInGroup(userName, subGroup)
                if answer:
                    break
    return answer


def first_test_case():
    parent = Group("parent")
    # No User Added. Expected answer false.
    print(isUserInGroup('parent_user', parent))


def second_test_case():
    # Valid user but with None or invalid group. Expected answer False.
    print(isUserInGroup('parent_user', None))


def third_test_case():
    firstGroup = Group("firstGroup")
    firstGroup.add_user("firstUser")
    # First user added to group. So should return True.
    print(isUserInGroup("firstUser", firstGroup))


first_test_case()
second_test_case()
third_test_case()
