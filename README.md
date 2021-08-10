# duiValidator
Validador de Dui escrito en python


Condiciones que se deben evaluar 
----------------------------------------
– El numero que esta a la derecha del guión se conoce como digito verificador
– Se coloca el numero sin guiones y con ceros a la izquierda
– Deben ser 9 caracteres
– Se toman los primeros 8 caracteres (sin el dígito verificador) y a cada uno se le multiplica por la posición en la que se encuentra. Partiendo que la posición 9 es el primer numero de la izquierda.
– Se suman todos los resultados
– Se hace un mod de la suma dividido por 10 (osea toma el remanente de esa división)
– Resta 10 menos el remanente de la division
– Si la resta da 0 el DUI es correcto
– Si la resta es igual al dígito verificador el DUI es correcto
– Si la resta es distinta al dígito verificador el DUI es incorrecto
