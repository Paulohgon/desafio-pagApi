from fastapi import APIRouter,Body,HTTPException
from presentation.pix import PixData
from datasource.sqldatabase import update,insert,get_all
from typing import List
import re
router = APIRouter()

@router.post("create/{receiver_id}", summary="create pix")
async def create_pix_by_receiver_id(receiver_id: int,
    pix_info: PixData = Body(...)):


    query = """
            insert into pix (receiver_id,pix,type,deleted,email)
            values ("{receiver_id}","{pix}","{type}","{deleted}","{email}");
            """.format(receiver_id=receiver_id, pix=pix_info.pix, type=pix_info.pix_type, deleted=False,email = pix_info.email)
    if validate_pix(pix_info.pix,pix_info.pix_type):    
        if pix_info.email:
            if await validate_email(pix_info.email):
                insert(query)
        else:
            insert(query)
    else:
        raise HTTPException(Status_code=405, detail="Invalid pix") 


async def validate_email(email:str):
    validation = re.compile(r"([A-Za-z0-9+.-_]+)+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
    return re.fullmatch(validation, email)


async def validate_pix(pix: str, pix_type: str):
    if pix_type == 'CPF':
        validation = re.compile(r"^[0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2}$")
        return re.fullmatch(validation, pix)         

    if pix_type == 'CNPJ':
        validation = re.compile(r"^[0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2}$")
        return re.fullmatch(validation, pix)
            
    if pix_type == 'EMAIL':
        validation = re.compile(r"([A-Za-z0-9+.-_]+)+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
        return re.fullmatch(validation, pix)
            
    if pix_type == 'TELEFONE':
        validation = re.compile(r"^((?:\+?55)?)([1-9][0-9])(9?[0-9]{8})$")
        return re.fullmatch(validation, pix)
            
    if pix_type == 'CHAVE_ALEATORIA':
        validation = re.compile(r"^((?:\+?55)?)([1-9][0-9])(9?[0-9]{8})$")
        return re.fullmatch(validation, pix)
              
    

@router.post("delete/{pix_id}", summary="delete pix")
async def delete_pix_by_receiver_id(pix_id: int):
    delete_pix = """update receiver set deleted = true
            where id = {pix_id}
            and deleted = false;""".format(pix_id=pix_id)
    update(delete_pix)

@router.get("/{receiver_id}", summary="get pix")
async def get_pix_by_receiver_id(receiver_id: int):
    get_pix = """select email,pix,type from pix
                    where receiver_id = {receiver_id}
                    and deleted = false;""".format(receiver_id=receiver_id)
    receiver_pix = get_all(get_pix)
    return receiver_pix