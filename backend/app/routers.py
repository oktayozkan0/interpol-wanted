from fastapi import APIRouter, Depends, Request
from database import DBMongo
from models import Criminal
import os
from fastapi_pagination import paginate
from fastapi.templating import Jinja2Templates
from pagination_settings import Page, Params


router = APIRouter(prefix="/api")
MONGO_COLLECTION = os.environ.get("MONGO_COLLECTION")

templates = Jinja2Templates(directory="templates")
mongo_db = DBMongo()

@router.get("/", response_model=Page[Criminal])
def get_criminals(request: Request, params: Params = Depends()):
    db = mongo_db.get_db()
    data = list(db[MONGO_COLLECTION].find({}, {"_id":0}))
    is_new_added = False
    if int(request.cookies["item_length"]) < len(data):
        is_new_added = True
    new_count = len(data) - int(request.cookies["item_length"])
    response = templates.TemplateResponse(
        "base.html", 
            {"request":request,
            "data": paginate(data, params),
            "new_item": is_new_added,
            "new_count": new_count}
    )
    response.set_cookie(key="item_length", value=f"{len(data)}")
    return response
