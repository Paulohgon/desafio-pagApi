from pydantic import BaseModel
from typing import Optional

class ReceiverDataReturn(BaseModel):

    receiver_id: int
    name: str
    cpf_cnpj: str
    bank: str
    agency: str
    cc: str
    validated: str
    email: str

class ReceiverDataCreate(BaseModel):

    name: str
    cpf_cnpj: str
    bank: str
    agency: str
    cc: str
    email: str
    validated: bool

class ReceiverDataUpdate(BaseModel):

    name: Optional[str]
    cpf_cnpj: Optional[str]
    bank: Optional[str]
    agency: Optional[str]
    cc: Optional[str]
    email: Optional[str]
    validated: Optional[bool]
