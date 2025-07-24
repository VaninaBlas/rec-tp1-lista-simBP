import unittest
# Se importa el codigo a testear.
from lista_simbp import simBP, lista_elementos_simBP_con_N

class TestListaSimBP(unittest.TestCase):
  
    def test_simBP_mismo_numero(self):
        # Ambos argumentos coinciden.
        self.assertEqual(simBP(1, 1), 1)  # 1
        self.assertEqual(simBP(5, 5), 3)  # 101
        self.assertEqual(simBP(8, 8), 4)  # 1000
        self.assertEqual(simBP(255, 255), 8)  # 11111111

    def test_simBP_n_menor_m(self):
        # El primer argumento es menor que el segundo
        self.assertEqual(simBP(1, 2), 1)  # 1     10
        self.assertEqual(simBP(1, 4), 1)  # 1    100
        self.assertEqual(simBP(3, 4), 1)  # 11   100
        self.assertEqual(simBP(3, 7), 2)  # 11   111
        self.assertEqual(simBP(4, 8), 3)  # 100  1000
        self.assertEqual(simBP(5, 15), 1) # 101  1111

    def test_simBP_n_mayor_m(self):
        # El primer argumento es mayor que el segundo
        self.assertEqual(simBP(2, 1), 1)  # 1     10
        self.assertEqual(simBP(4, 1), 1)  # 1    100
        self.assertEqual(simBP(4, 3), 1)  # 11   100
        self.assertEqual(simBP(7, 3), 2)  # 11   111
        self.assertEqual(simBP(8, 4), 3)  # 100  1000
        self.assertEqual(simBP(15, 5), 1) # 101  1111

    def test_simBP_prefijos(self):
        # La representación binaria de un número es prefijo de la del otro.
        self.assertEqual(simBP(5, 10), 3)  # 101  1010
        self.assertEqual(simBP(10, 5), 3)  # 101  1010
        self.assertEqual(simBP(45, 22), 5) # 10110 101101
        self.assertEqual(simBP(22, 45), 5) # 101101 10110

    def test_simBPN_numeros_grandes(self):
        # Probamos algunos números "grandes".
        # ** es el operador para calcular potencias (a**b es a elevado a la b).
        self.assertEqual(simBP(2**30, 2**30), 31)      # 100...00  100...00
        self.assertEqual(simBP(2**30, 2**30 - 1), 1)   # 100...00   11...11
        self.assertEqual(simBP(2**30, 2**30 + 1), 30)  # 100...00  100...01
        self.assertEqual(simBP(2**30-1, 2**30-1),   30)  #  11...11   11...11

  #### Abreviamos lescn = lista_elementos_simBP_con_N

    def test_lescn_igual_simbp(self):
        # Todos los elementos tienen la misma simbp con n
        self.assertEqual(lista_elementos_simBP_con_N(3,[50,60,99,123,13]),[2, 2, 2, 2, 2])
        self.assertEqual(lista_elementos_simBP_con_N(2,[16,23,45,89,76]),[2,2,2,2,2])
        self.assertEqual(lista_elementos_simBP_con_N(5,[179,11,189,190,22]),[3,3,3,3,3])
        self.assertEqual(lista_elementos_simBP_con_N(7,[124,999,468,984,489]),[3,3,3,3,3])

    def test_lescn_lista_numeros_grandes(self):
        #Probamos usando numeros "grandes" en la lista
        # ** es el operador para calcular potencias (a**b es a elevado a la b).
        self.assertEqual(lista_elementos_simBP_con_N(3,[12**5,30**6,30**4, 18**7, 29**3]),[2,1, 2, 1, 1])
        self.assertEqual(lista_elementos_simBP_con_N(5,[38**6,24**6,19**4,22**6,21**7]),[3,3,1,1,1])
        self.assertEqual(lista_elementos_simBP_con_N(13,[19**7,28**6,31**6,26**5,34**5]),[4,2,4,1,1])
        self.assertEqual(lista_elementos_simBP_con_N(22,[35**5,22**6,26**6,30**5,28**4]),[1,1,2,4,2])
        self.assertEqual(lista_elementos_simBP_con_N(26,[31**3,29**5,27**6,30**4,26**7]),[2,1,1,3,2])
    def test_lescn_n_mayor_numero(self):
        # n es mayor a los elementos de lista
        self.assertEqual(lista_elementos_simBP_con_N(12**6, [23,45,12,87,43]), [4, 6, 1, 3, 3])
        self.assertEqual(lista_elementos_simBP_con_N(18**5,[12,56,37,58,99]),[2,5,1,4,2])
        self.assertEqual(lista_elementos_simBP_con_N(11**3,[14,38,90,78,49]),[1,2,3,2,1])
        self.assertEqual(lista_elementos_simBP_con_N(5**9,[23,48,99,6,88]),[1,2,2,2,1])
    def test_lescn_mismos_numeros(self):
        #n y todos los elementos de la lista son los mismos
        self.assertEqual(lista_elementos_simBP_con_N(12,[12,12,12,12,12]),[4,4,4,4,4])
        self.assertEqual(lista_elementos_simBP_con_N(20,[20,20,20,20,20]),[5,5,5,5,5])
        self.assertEqual(lista_elementos_simBP_con_N(55,[55,55,55,55,55]),[6,6,6,6,6])
        self.assertEqual(lista_elementos_simBP_con_N(33,[33,33,33,33,33]),[6,6,6,6,6])
    def test_lescn_simbp_menor_a_mayor(self):
        # las simbps entre n y los elementos de lista van de menor a mayor (1,4,5,7)
        self.assertEqual(lista_elementos_simBP_con_N(12,[10,7,13,50]),[1,2,3,4])
        self.assertEqual(lista_elementos_simBP_con_N(52,[2,7,24,111,3444,104]),[1,2,3,4,5,6])
        self.assertEqual(lista_elementos_simBP_con_N(11,[3,2,5,22]),[1,2,3,4])
        self.assertEqual(lista_elementos_simBP_con_N(20,[3,34,5,43,40]),[1,2,3,4,5])

    def test_lescn_simbp_mayor_a_menor(self):
        # las simbps entre n y los elementos de lista van de mayor a menor (7,4,5,1)
        self.assertEqual(lista_elementos_simBP_con_N(12,[50,13,7,10]),[4,3,2,1])
        self.assertEqual(lista_elementos_simBP_con_N(27,[54,53,98,14,5]),[5,4,3,2,1])
        self.assertEqual(lista_elementos_simBP_con_N(34,[68,35,8,38,80,7]),[6,5,4,3,2,1])
        self.assertEqual(lista_elementos_simBP_con_N(79,[158,39,304,18,66,10,3]),[7,6,5,4,3,2,1])

    def test_lescn_lista_numeros_doble_al_anterior(self):
        # los elementos de lista son el doble del anterior (n, (a=n*2,b=a*2,c=b*2, d=c*2))
        self.assertEqual(lista_elementos_simBP_con_N(12,[24,48,96,192]),[4,4,4,4])
        self.assertEqual(lista_elementos_simBP_con_N(22,[44,88,176,352]),[5,5,5,5])
        self.assertEqual(lista_elementos_simBP_con_N(10,[20,40,80,160]),[4,4,4,4])
        self.assertEqual(lista_elementos_simBP_con_N(8,[16,32,64,128]),[4,4,4,4])
    def test_lescn_lista_numeros_impares(self):
        # los elementos de lista son numeros impares (num%2!=0)
        self.assertEqual(lista_elementos_simBP_con_N(12,[11,13,17,19,23]),[1,3,1,1,1])
        self.assertEqual(lista_elementos_simBP_con_N(16,[5,29,37,15,99]),[2,1,3,1,1])
        self.assertEqual(lista_elementos_simBP_con_N(25,[9,47,33,97,31]),[1,1,1,4,2])
        self.assertEqual(lista_elementos_simBP_con_N(32,[89,37,43,61,77]),[2,3,2,1,3])

    def test_lescn_igual_longitud_binaria(self):
        # los elementos de lista y n tienen la misma longitud binaria
        self.assertEqual(lista_elementos_simBP_con_N(101, [103,111,97,81,83]),[5,3,4,1,1]) # longitud de 7 bits
        self.assertEqual(lista_elementos_simBP_con_N(56,[34,48,60,44,39]),[1,2,3,1,1])# longitud de 6 bits
        self.assertEqual(lista_elementos_simBP_con_N(290,[306,498,499,483,451]),[4,1,1,1,1]) # longitud de 9 bits
        self.assertEqual(lista_elementos_simBP_con_N(200, [142,204,233,218,128]),[1,5,2,3,1]) # longitud de 8 bits

    def test_lescn_simbp_par(self):
        #las simbps entre n y los elementos de lista son numeros pares (2,4,2,2,4)
        self.assertEqual(lista_elementos_simBP_con_N(1000,[250,1003,15,3,62]),[8,8,4,2,6])	  
        self.assertEqual(lista_elementos_simBP_con_N(560,[67,1126,23,287,46]),[4,8,2,6,2])
        self.assertEqual(lista_elementos_simBP_con_N(900,[48,905,237,3613,14]),[2,6,4,8,4])
        self.assertEqual(lista_elementos_simBP_con_N(230,[118,25,457,99,109]),[4,2,6,2,2])
    def test_lescn_lista_numeros_multiplos_de_n(self):
        # los elementos de lista son multiplos de n
        self.assertEqual(lista_elementos_simBP_con_N(12,[12,24,36,48,60]),[4,4,1,4,2])
        self.assertEqual(lista_elementos_simBP_con_N(8,[16,24,32,40,48]),[4,1,4,2,1])
        self.assertEqual(lista_elementos_simBP_con_N(5,[15,10,25,30,50]),[1,3,1,1,1])
        self.assertEqual(lista_elementos_simBP_con_N(10,[40,50,100,120,70]),[4,1,1,1,2])
        self.assertEqual(lista_elementos_simBP_con_N(2,[6,4,8,10,14]),[1,2,2,2,1])
    def test_lescn_lista_vacia(self):
        # la lista es vacia
        self.assertEqual(lista_elementos_simBP_con_N(12, []), [])
        self.assertEqual(lista_elementos_simBP_con_N(20,[]),[])
        self.assertEqual(lista_elementos_simBP_con_N(1,[]),[])
        self.assertEqual(lista_elementos_simBP_con_N(98,[]),[])
    def test_lescn_n_dentro_de_lista(self):
        # n es un elemento de la lista
        self.assertEqual(lista_elementos_simBP_con_N(250, [789,43,250,98,12]),[2,1,8,2,2])	 
        self.assertEqual(lista_elementos_simBP_con_N(87,[23,32,45,123,87]),[3,2,3,1,7])
        self.assertEqual(lista_elementos_simBP_con_N(340,[550,768,901,340,3210]),[2,1,1,9,1])
        self.assertEqual(lista_elementos_simBP_con_N(671,[671,236,545,1290,43]),[10,1,2,5,4])
    def test_lescn_lista_solo_un_elemento(self):
        # la lista solo tiene un elemento
        self.assertEqual(lista_elementos_simBP_con_N(12, [11]),[1])
        self.assertEqual(lista_elementos_simBP_con_N(13,[123]),[2])
        self.assertEqual(lista_elementos_simBP_con_N(21,[87]),[5])
        self.assertEqual(lista_elementos_simBP_con_N(98,[450]),[2])
    def test_lescn_simbp_uno(self):
        # las simbp entre n y los elementos de la lista son todos de 1
        self.assertEqual(lista_elementos_simBP_con_N(12,[1,1,1,1,1]),[1,1,1,1,1])
        self.assertEqual(lista_elementos_simBP_con_N(5,[54,12,98,55,123]), [1,1,1,1,1])
        self.assertEqual(lista_elementos_simBP_con_N(6,[90,76,129,170,560]), [1,1,1,1,1])  
        self.assertEqual(lista_elementos_simBP_con_N(2,[24,388,239,6212,987]),[1,1,1,1,1])
    def test_lescn_simbp_alta(self):
	 # las simbp entre n y los elementos de la lista es muy "alta"
        self.assertEqual(lista_elementos_simBP_con_N(700,[175,43,350,21,87]),[8,6,9,5,7])
        self.assertEqual(lista_elementos_simBP_con_N(1640,[414,13134,1643,811,13126]),[6,10,9,5,11])
        self.assertEqual(lista_elementos_simBP_con_N(10500,[2639,21023,5262,42007,84005]),[8,10,9,13,14])
        self.assertEqual(lista_elementos_simBP_con_N(7890,[15791,1969,63126,31554,15806]),[10,8,13,11,9])
        
unittest.main()