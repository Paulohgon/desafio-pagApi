from src.entrypoints.pix import validate_pix
from src.presentation.pix import PixData


def func_validation(testpix):
    print ("paozinho",validate_pix(testpix.pix, testpix.pix_type))
    if validate_pix(testpix.pix, testpix.pix_type):
        return True
    else:
        return False


class TestClass:


    def test_answer(self):
        pix_teste = PixData(pix_type ="EMAIL", pix = "paulohgon01@gmail.com", email="paulohgon01@gmail.com")
        assert func_validation(pix_teste) == True
        

    def test_answer2(self):
        pix_teste = PixData(pix_type ="CPF", pix = "152.555.555-98", email="paulohgon01@gmail.com")
        assert func_validation(pix_teste) == True
        

    def test_answer3(self):
        pix_teste = PixData(pix_type ="CNPJ", pix = "11.111.111/0001-11", email="paulohgon01@gmail.com")
        assert func_validation(pix_teste) == True
        

    def test_answer4(self):
        pix_teste = PixData(pix_type ="TELEFONE", pix = "+5547988443333", email="paulohgon01@gmail.com")
        assert func_validation(pix_teste) == True

    def test_answer5(self):
        pix_teste = PixData(pix_type = "CHAVE_ALEATORIA", pix = "dbbf965d-677c-49ff-b9da-5131da1505f3",email= "paulohgon01@gmail.com")
        assert func_validation(pix_teste) == True
        
