from src.presentation.receiver import ReceiverDataCreate

def func_validation(receiver):
    
    if receiver == "Paulo Henrique" and receiver.cpf_cnpj == "125.255.255-25" \
    and receiver.bank == "itau" and receiver.agency == "0123" and receiver.cc == "000012345-6" and receiver.validated == True and receiver.email == "paulo@gmail.com":
        return True
    else:
        return False


class TestClass:

    def test_created(self):
        receiver_test = ReceiverDataCreate(name ="Paulo henrique", 
        cpf_cnpj= "125.255.255-25", bank="itau",
        agency="0123",cc="000012345-6",email="paulo@gmail.com",validated=True)
        return func_validation(receiver_test)== True