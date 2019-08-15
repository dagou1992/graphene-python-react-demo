from db_utils import ModelUtil

map_name = 'user'
table_name = 'User'


class User:

    @classmethod
    def get_user(cls, id):
        conditions = {"id": id} if id else None
        s = ModelUtil.query_many(map_name, table_name, conditions, {'_id': 0})
        return s

    @classmethod
    def update_user(cls, data):
        item = ModelUtil.query_one(map_name, table_name, {"id": data['id']})
        for k, v in data.items():
            if k in item.keys() and v:
                item[k] = v
        ModelUtil.update(map_name, table_name, item)
        item.pop("_id")
        return item

    @classmethod
    def create_user(cls, data):
        u = list(ModelUtil.query_many(map_name, table_name))
        data['id'] = int(u[len(u) - 1]['id']) + 1
        item = ModelUtil.create(map_name, table_name, data)
        item.pop("_id")
        return item

    @classmethod
    def delete_user(cls, id):
        item = ModelUtil.delete(map_name, table_name, {"id": id})
        return item