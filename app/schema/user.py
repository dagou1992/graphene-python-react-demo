from graphene import Interface, ID, String, Int, ObjectType, List


class User(Interface):
    id = ID()
    username = String()
    created_time = Int()
    role = Int()


class UserObjectType(ObjectType):
    class Meta:
        interfaces = (User,)
