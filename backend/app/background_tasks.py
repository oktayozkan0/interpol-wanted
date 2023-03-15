import threading
from consumer import to_mongo

class BackgroundTask(threading.Thread):
    def run(self,*args,**kwargs):
        to_mongo()
