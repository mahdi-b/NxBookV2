
from vue.utils import js_lib
from vue.bridge import Object
from javascript import JSON
from browser import aio as asyncio, window

import sqlite3
SQLITE3_DB_PATH = "/ABCD"

class NxFirebaseBackEnd:
    def __init__(self):

        self.database = sqlite3.connect(SQLITE3_DB_PATH)



    async def get_modules(self):
        """Returns all the modules in the db"""
        data = []
        def extract_data(js_object):
            print("extract data 1")

            nonlocal data

            js_object.forEach(lambda x: data.append({"value": x.id, "text": x.data().complete_name}))
            print(f"--1 -- {data}")
        def get_error(err):
            print(f"Error occurred while parsing firebase response for modules. Code: {err.code}")

        await self.database\
            .collection("modules")\
            .get()\
            .then(extract_data)\
            .catch(get_error)

        return data

    def get_object_repr(self, obj):
        dict_repr = {}
        for field in dir(obj):
            """Error can occur here with, for example
             lists that have null. Use print to see what cause the isseu"""
            # print(f"value for field: {field} is {getattr(obj, field)}")
            dict_repr[field] = getattr(obj, field)
        return dict_repr

    async def get_questions(self, module_name):
        """Returns all the questions associated with module_name"""

        data = []

        print(f"getting questions for module: {module_name}")
        ref = self.database.collection(f"questions/module/{module_name}")
        promise = await ref.get()
        # Better to do it with then and else!
        promise.forEach(
            lambda x: data.append({"value": x.id,
                                   "data": self.get_object_repr(x.data())})
        )
        print(f"--1 -- {data}")
        return data




