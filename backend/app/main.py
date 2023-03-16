from fastapi import FastAPI
import routers
import uvicorn
from background_tasks import BackgroundTasks
import time


app = FastAPI()

app.include_router(routers.router)

if __name__ == "__main__":
    time.sleep(20)
    t = BackgroundTasks()
    t.start()
    uvicorn.run(app, host="0.0.0.0", port=8001)
