from graphene import ObjectType, Schema, Field, List, Int
from .user import User, UserObjectType
from .workload import Workload
from app.muation.user import UserMutation
from app.models.user import User as userModal


class Mutations(ObjectType):
    userMutation = UserMutation.Field()


class Query(ObjectType):
    user = Field(List(lambda: UserObjectType), id=Int())
    workload = Field(List(lambda: Workload), id=Int())

    @staticmethod
    def resolve_user(self, info, id=None):
        return userModal.get_user(id)

    @staticmethod
    def resolve_workload(self, info, id=None):
        return userModal.get_user(id)


schema = Schema(query=Query, mutation=Mutations)