import threading
from consumer import to_mongo

class BackgroundTasks(threading.Thread):
    def run(self,*args,**kwargs):
        to_mongo()
