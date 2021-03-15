
from vue.utils import js_lib
from vue.bridge import Object
from javascript import JSON
from browser import aio as asyncio, window

class NxFirebaseBackEnd:
    def __init__(self):
        firebase_cfg = {
            "apiKey": "AIzaSyCY_PJg7LPLpW0J0nfml1LWjBMFv63WKtQ",
            "authDomain": "nxbook.firebaseapp.com",
            "databaseURL": "https://nxbook.firebaseio.com",
            "projectId": "nxbook",
            "storageBucket": "nxbook.appspot.com",
            "messagingSenderId": "451664479402",
            "appId": "1:451664479402:web:ad7aec578e40cfffe5bcd3"
        }

        self.firebase = js_lib("firebase")
        self.firebase.initializeApp(Object.to_js(firebase_cfg))

        self.database = self.firebase.firestore()



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




