import unittest

from num2rus.main import converter


class TestconverterEURtests(unittest.TestCase):
    def test_651_000_000_000_00(self):
        result = converter(651_000_000_000, currency="EUR", zero_on=False)
        self.assertEqual(result, 'шестьсот пятьдесят один миллиард евро')
    def test_zero_on_651_000_000_000z_00(self):
        result = converter(651_000_000_000, currency="EUR")
        self.assertEqual(result, 'шестьсот пятьдесят один миллиард евро ноль центов')
    def test_651_000_000_000z_04_only_number(self):
        result = converter(651_000_000_000.01, only_rubles=True, only_number=True, currency="EUR")
        self.assertEqual(result, 'шестьсот пятьдесят один миллиард')
    def test_651_000_000_000z_04_only_numder(self):
        result = converter(651_000_000_000.01, only_rubles=True, currency="EUR")
        self.assertEqual(result, 'шестьсот пятьдесят один миллиард евро')
    def test_651_000_000_001z_04_only_numder(self):
        result = converter(651_000_000_001.01, only_rubles=True, currency="EUR")
        self.assertEqual(result, 'шестьсот пятьдесят один миллиард один евро')
    def test_651_000_000_001z_only_rubles_only_number(self):
        result = converter(651_000_000_001.01, only_rubles=True, only_number=True, currency="EUR")
        self.assertEqual(result, 'шестьсот пятьдесят один миллиард один')
    def test_651_000_000_001z21(self):
        result = converter(651_000_000_001.21, currency="EUR")
        self.assertEqual(result, 'шестьсот пятьдесят один миллиард один евро двадцать один цент')
    def test_z21(self):
        result = converter(0.21, currency="EUR")
        self.assertEqual(result, 'ноль евро двадцать один цент')
    def test_1z21(self):
        result = converter(1.21, currency="EUR")
        self.assertEqual(result, 'один евро двадцать один цент')
    def test_1z21_only_rubles(self):
        result = converter(1.21, currency="EUR", only_rubles=True)
        self.assertEqual(result, 'один евро')
    def test_1z21_only_number(self):
        result = converter(1.21, currency="EUR", only_rubles=True, only_number=True)
        self.assertEqual(result, 'один')
    def test_12345678z24(self):
        result = converter(12345678.24, currency="EUR")
        self.assertEqual(result, 'двенадцать миллионов триста сорок пять тысяч шестьсот семьдесят восемь евро двадцать четыре цента')
    def test_1z01(self):
        result = converter(1.01, currency="EUR")
        self.assertEqual(result, 'один евро один цент')
    def test_22z02(self):
        result = converter(22.02, currency="EUR")
        self.assertEqual(result, 'двадцать два евро два цента')

if __name__ == '__main__':
    unittest.main()
