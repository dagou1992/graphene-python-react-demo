from config import client
import time


def timestamp():
    return int(time.time())


class ModelUtil():

    @classmethod
    def create(cls, db_name, table_name, item):
        mongua = client[db_name]
        table = mongua[table_name]
        item["deleted"] = False
        ts = timestamp()
        item["created_time"] = ts
        item["updated_time"] = ts
        table.insert_one(item)
        return item


    @classmethod
    def query_one(cls, db_name, table_name, conditions, exists=True):
        mongua = client[db_name]
        table = mongua[table_name]
        if exists:
            if conditions is not None:
                conditions['deleted'] = False
            else:
                conditions = {'deleted': False}
        item = table.find_one(conditions)
        return item

    @classmethod
    def query_many(cls, db_name, table_name, conditions=None, projection=None, exists=True):
        mongua = client[db_name]
        table = mongua[table_name]
        if exists:
            if conditions is not None:
                conditions['deleted'] = False
            else:
                conditions = {'deleted': False}
        item = table.find(conditions, projection)
        return item

    @classmethod
    def update(cls, db_name, table_name, item):
        mongua = client[db_name]
        table = mongua[table_name]
        item["updated_time"] = timestamp()
        table.save(item)
        return item

    @classmethod
    def delete(cls, db_name, table_name, conditions):
        item = cls.query_one(db_name, table_name, conditions)
        item["deleted"] = True
        cls.update(db_name, table_name, item)
        return item