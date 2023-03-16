from fastapi import FastAPI
import routers
import uvicorn
from background_tasks import BackgroundTask
import time


app = FastAPI()

app.include_router(routers.router)

if __name__ == "__main__":
    time.sleep(20)
    task = BackgroundTask()
    task.start()
    uvicorn.run(app, host="0.0.0.0", port=8001)
