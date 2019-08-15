from graphene import Int, Mutation, Field, String, ObjectType
from app.schema.user import User
from app.models.user import User as userModal


class UserInput(ObjectType):
    class Meta:
        interfaces = (User, )
    type = String()


class UserMutation(Mutation):
    class Arguments:
        id = Int()
        role = Int()
        username = String()
        type = String()

    user = Field(UserInput)

    @staticmethod
    def mutate(root, info, type, role=None, id=None, username=None):
        if type == 'create':
            user = userModal.create_user(dict(username=username, role=role))
        elif type == 'update':
            user = userModal.update_user(dict(id=id, role=role, username=username))
        elif type == 'delete':
            user = userModal.delete_user(id)
        return UserMutation(user)