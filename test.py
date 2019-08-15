from graphene import ObjectType, String, Schema, List, Enum, Interface, ID, Field


class Episode(Enum):
    NEWHOPE = 4
    EMPIRE = 5
    JEDI = 6


class Character(Interface):
    id = ID()
    name = String()
    friends = List(lambda: Character)
    appears_in = List(Episode)

    def resolve_friends(self, info):
        # The character friends is a list of strings
        return [get_character(f) for f in self.friends]

class Human(ObjectType):
    class Meta:
        interfaces = (Character,)

    home_planet = String()

d = Human(
        id="1000",
        name="Luke Skywalker",
        friends=["1002", "1003", "1003", "1003"],
        appears_in=[4, 5, 6],
        home_planet="Tatooine",
    )

human_data = {
        "1000": d,
        "1001": d,
        "1002": d,
        "1003": d,
        "1004": d,
    }

def get_character(id):
    return human_data.get(id)

def get_hero(episode):

    return d

class Query(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    hello = String()
    goodbye = String()
    hero = Field(Character)
    human = Field(Human)

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    @staticmethod
    def resolve_hello(root, info):
        return 'hello'

    @staticmethod
    def resolve_goodbye(root, info):
        return 'See ya!'

    def resolve_hero(self, info, episode=None):
        return get_hero(episode)

schema = Schema(query=Query)