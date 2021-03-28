# import firebase_admin
# from firebase_admin import credentials
# import threading

# class MessageHandler(object):
#     _instance_lock = threading.Lock()
 
#     def __init__(self):
#         if not hasattr(self, 'app'):
#             with MessageHandler._instance_lock:
#                 if not hasattr(self, 'app'):
#                     self.cred = credentials.Certificate('/home/sara/Documents/Wactop/wactop-20230-firebase-adminsdk-yf4ps-57e8a0ccd2.json')
#                     self.default_app = firebase_admin.initialize_app(self.cred)
#                     self.app = self.default_app
 
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(MessageHandler, "_instance"):
#             with MessageHandler._instance_lock:
#                 if not hasattr(MessageHandler, "_instance"):
#                     MessageHandler._instance = object.__new__(cls)
#         return MessageHandler._instance
 
#     def get_app(self):
#         return self.app
 
 
# _message_handler = MessageHandler()
 
 
# if '__name__' == 'main':
#     print('register success!')
 
