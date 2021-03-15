# import firebase_admin
# from firebase_admin import credentials, firestore
#
#
# class NxFireBaseStorage:
#
#     def __init__(self):
#         firebase_admin.initialize_app()
#         self.firestore_db = firestore.client()
#
#     def list_modules(self):
#         return [x.todict() for x in self.firestore_db.collection(u'songs').get()]
#
#
#
