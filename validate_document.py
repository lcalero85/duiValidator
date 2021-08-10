import re


class validate_document(object):

    def __init__(self):
        super(validate_document, self)

        self.patron = re.compile("^\\d{8}-\\d$")

    def validate_id_number(self, dui):

        global residuoVerificador, residuo
        if self.patron.match(dui):
            digitoVerificador = int(dui[9])
            print(digitoVerificador)

            numero = 10
            cadenaDui = dui[0:8]
            sum = 0
            for indice in range(len(cadenaDui)):
                caracter = cadenaDui[indice]
                numero = numero - 1
                sum = sum + (numero * int(caracter))
                residuo = sum % 10
                if residuo > 0:
                    residuo = residuo - 10
            if abs(residuo) == digitoVerificador or residuo == 0:
                print(" Dui Valido")
                return True
            else:
                print("Dui invalido")
                return False
        else:
            print("Unrecognized pattern")
