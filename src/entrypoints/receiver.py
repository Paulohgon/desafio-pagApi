from fastapi import APIRouter,Body,HTTPException
from presentation.receiver import ReceiverDataReturn,ReceiverDataCreate,ReceiverDataUpdate
from datasource.sqldatabase import get_one,get_all,insert,update,updateMany
from typing import List
import re
router = APIRouter()


@router.get("/all", response_model=List[ReceiverDataReturn], summary="Get Receivers infos")
async def get_receivers():

    receivers_list = list()
    
    query = """
    select id,name,cpf as cpf_cnpj, bank,agency,cc,email,validated from receiver where deleted = false;
    """

    receivers = get_all(query)
    print(receivers)
    for receiver in receivers:
        receivers_dict = {}
        receivers_dict['receiver_id'] = receiver[0]
        receivers_dict['name'] = receiver[1]
        receivers_dict['cpf_cnpj'] = receiver[2]
        receivers_dict['bank'] = receiver[3]
        receivers_dict['agency'] = receiver[4]
        receivers_dict['cc'] = receiver[5]
        receivers_dict['email'] = receiver[6]
        receivers_dict['validated'] = receiver[7]
        receivers_list.append(receivers_dict)



    return receivers_list

@router.get("/{receiver_id}", response_model=ReceiverDataReturn, summary="Get a Receiver info by id")
async def get_receiver_by_id(receiver_id):

    receiver_dict = {}
    query = """
    select id,name,cpf as cpf_cnpj,bank,agency,cc,email,validated
    from receiver where id = {receiver_id} and deleted = false;
    """.format(receiver_id=receiver_id)

    receiver = get_one(query)
    print(receiver)

    if receiver is None:
        raise HTTPException(status_code=404, detail="user not found")
        
    receiver_dict['receiver_id'] = receiver[0]
    receiver_dict['name'] = receiver[1]
    receiver_dict['cpf_cnpj'] = receiver[2]
    receiver_dict['bank'] = receiver[3]
    receiver_dict['agency'] = receiver[4]
    receiver_dict['cc'] = receiver[5]
    receiver_dict['email'] = receiver[6]
    receiver_dict['validated'] = receiver[7]

    return receiver_dict

@router.post("/create", summary="Create new receiver")
async def create_receiver(
    new_receiver: ReceiverDataCreate = Body(...)
):
    query = """
    insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
    values ("{name}","{cpf}","{bank}","{agency}","{cc}",{validated},"{email}",{deleted});
    """.format(name=new_receiver.name, cpf=new_receiver.cpf_cnpj,
            bank=new_receiver.bank,
            agency=new_receiver.agency,
            cc=new_receiver.cc,
            validated=False,
            email=new_receiver.email,
            deleted=False)
    insert(query)


@router.post("/update/{receiver_id}", summary="Update receiver")
async def update_by_receiver_id(receiver_id: int,
                                new_infos: ReceiverDataUpdate = Body(...)):
    selected_receiver = await get_receiver_by_id(receiver_id)
    is_validated = selected_receiver['validated']
    print(type(is_validated))
    if is_validated:
        update_query = """
        update receiver set
        email = {new_email} where receiver_id = {receiver_id}
        and deleted = false;
        """.format(new_email=new_infos.email, receiver_id=receiver_id)
        updateMany(update_query)

    else:
        update_query =''
        updates_list = list()

        if new_infos.name:
            update_name = """update receiver set name = "{new_name}"
            where id = {receiver_id}
            and deleted = false;""".format(receiver_id=receiver_id, new_name=new_infos.name)
            update_query = f"{update_query} {update_name}"
            updates_list.append(update_name)
        if new_infos.cpf_cnpj:

            update_cpf_cnpj = """update receiver set cpf = "{new_cpf_cnpj}"
            where id = {receiver_id}
            and deleted = false;""".format(receiver_id=receiver_id, new_cpf_cnpj=new_infos.cpf_cnpj)
            updates_list.append(update_cpf_cnpj)
            update_query = f"{update_query} {update_cpf_cnpj}"


        if new_infos.email:
            
            update_email = """update receiver set email = "{new_email}"
            where id = {receiver_id}
            and deleted = false;""".format(receiver_id=receiver_id, new_email=new_infos.email)
            updates_list.append(update_email)
            update_query = f"{update_query} {update_email}"

        if new_infos.bank:

            update_bank = """update receiver set bank = "{new_bank}"
            where id = {receiver_id}
            and deleted = false;""".format(receiver_id=receiver_id, new_bank=new_infos.bank)
            update_query = f"{update_query} {update_bank}"

        if new_infos.agency:
            update_agency = """update receiver set agency = "{new_agency}"
            where id = {receiver_id}
            and deleted = false;""".format(receiver_id=receiver_id, new_agency=new_infos.agency)
            update_query = f"{update_query} {update_agency}"
        if new_infos.cc:

            update_cc = """update receiver set cc = "{new_cc}"
            where id = {receiver_id}
            and deleted = false;""".format(receiver_id=receiver_id, new_cc=new_infos.cc)
            update_query = f"{update_query} {update_cc}"
            updates_list.append(update_cc)

        updateMany(update_query)
