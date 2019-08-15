from graphene import ObjectType, List, String
from .user import User


class Workload(ObjectType):
    class Meta:
        interfaces = (User, )

    imgs = List(String)