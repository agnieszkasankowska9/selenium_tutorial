import unittest
from TDD.aplikacja import Czlowiek

class TestCzlowiek(unittest.TestCase):
    #setup zrobi się przed każdym testem
    def setUp(self):
        self.czlowiek = Czlowiek("Stasio")
        #print("Przygotowanie testu")
        pass
    # metody testowe
    # zaczynają się od słowa "test"
    # testy wykonają się w dowolnej kolejności
    def test_przedstaw_się(self):
        przedstawienie_str = self.czlowiek.przedstaw.sie()
        self.assertEqual("Cześć, jestem Stasio", przedstawienie_str)
        pass
    # def testDrugi(self):
    #     #print("Test drugi")
    #     self.assertEqual(1,1)
    #     pass
    # # zrobi się po każdym teście
    # def tearDown(self):
    #     #print("Koniec testu")
    #     pass

if __name__ == "__main__":
    unittest.main(verbosity=2) #gadatliwość: 0,1,2
