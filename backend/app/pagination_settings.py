from fastapi_pagination.default import Page as BasePage, Params as BaseParams
from typing import TypeVar, Generic
from fastapi import Query

T = TypeVar("T")

class Params(BaseParams):
    size: int = Query(12, ge=1, le=24, description="Page size")

class Page(BasePage[T], Generic[T]):
    __params_type__ = Params
