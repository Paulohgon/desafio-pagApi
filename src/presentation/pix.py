from pydantic import BaseModel
from typing import Optional

class PixData(BaseModel):
    raceiver_id: int
    pix_type: str
    pix: str
    email: Optional[str]