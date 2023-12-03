import unittest
from Matice import Matice


class MatrixTestCase(unittest.TestCase):

    def test_vytvoreni_matice(self):
        matice = Matice(2, 2)
        matice.set_value(0, 0, 10)
        matice.set_value(0, 1, 20)
        matice.set_value(1, 0, 30)
        matice.set_value(1, 1, 40)

        self.assertEqual(matice.get_value(0, 0), 10)
        self.assertEqual(matice.get_value(0, 1), 20)
        self.assertEqual(matice.get_value(1, 0), 30)
        self.assertEqual(matice.get_value(1, 1), 40)

    def test_pocet_zadanych_hodnot_matice(self):
        matice = Matice(2, 2)
        matice.set_value(0, 0, 2)
        matice.set_value(0, 1, 5)
        matice.set_value(1, 0, 5)
        matice.set_value(1, 1, 7)

        self.assertEqual(matice.get_values_count(5), 2)
        self.assertEqual(matice.get_values_count(2), 1)
        self.assertEqual(matice.get_values_count(7), 1)
        self.assertEqual(matice.get_values_count(8), 0)

    def test_pocet_prazdnych_hodnot_matice(self):
        matice = Matice(10, 10)
        matice.set_value(3, 5, 2)
        matice.set_value(9, 9, 7)

        self.assertEqual(matice.get_empty_values_count(), 98)
        self.assertEqual(matice.get_values_count(), 2)

    def test_vyhledani_v_matici(self):
        matice = Matice(2, 2)
        matice.set_value(0, 0, 10)
        matice.set_value(0, 1, 20)
        matice.set_value(1, 0, 30)
        matice.set_value(1, 1, 40)

        self.assertTrue(10 in matice)
        self.assertFalse(100 in matice)
        self.assertTrue(20 in matice)

    def test_rozmery_matice(self):
        matice = Matice(3, 2)
        matice.set_value(0, 0, 10)
        matice.set_value(0, 1, 20)
        matice.set_value(1, 0, 30)
        matice.set_value(1, 1, 40)
        matice.set_value(2, 0, 50)
        matice.set_value(2, 1, 60)

        self.assertEqual(matice.get_pocet_radku(), 3)
        self.assertEqual(matice.get_pocet_sloupcu(), 2)

    def test_prohozeni_radku_a_sloupcu_matice(self):
        matice = Matice(3, 2)
        matice.set_value(0, 0, 10)
        matice.set_value(0, 1, 20)
        matice.set_value(1, 0, 30)
        matice.set_value(1, 1, 40)
        matice.set_value(2, 0, 50)
        matice.set_value(2, 1, 60)

        self.assertEqual(matice.get_pocet_radku(), 3)
        self.assertEqual(matice.get_pocet_sloupcu(), 2)

        matice.transponovat()  # Vymenit radky a sloupce

        self.assertEqual(matice.get_pocet_radku(), 2)
        self.assertEqual(matice.get_pocet_sloupcu(), 3)

        self.assertEqual(matice.get_value(0, 0), 10)
        self.assertEqual(matice.get_value(0, 1), 30)
        self.assertEqual(matice.get_value(0, 2), 50)
        self.assertEqual(matice.get_value(1, 0), 20)
        self.assertEqual(matice.get_value(1, 1), 40)
        self.assertEqual(matice.get_value(1, 2), 60)


if __name__ == '__main__':
    try:
        unittest.main()
    except Exception as e:
        print(e)
