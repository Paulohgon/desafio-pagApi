from fastapi import APIRouter
from datasource.sqldatabase import create_database
from typing import List
router = APIRouter()

@router.get("/create",  summary="Create database")
async def create_data_base():
    (create_database())
