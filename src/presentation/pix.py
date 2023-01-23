from pydantic import BaseModel
from typing import Optional

class PixData(BaseModel):
    pix_type: str
    pix: str
    email: Optional[str]

class PixDataReturns(BaseModel):
    raceiver_id: int
    pix_type: str
    pix: str
    email: Optional[str]