import unittest

from num2rus.main import converter


class TestconverterCHYtests(unittest.TestCase):
    def test_651_000_000_000_00(self):
        result = converter(651_000_000_000, currency="CNY", zero_on=False)
        self.assertEqual(result, 'шестьсот пятьдесят один миллиард юаней')
    def test_zero_on_651_000_000_000z_00(self):
        result = converter(651_000_000_000, currency="CNY")
        self.assertEqual(result, 'шестьсот пятьдесят один миллиард юаней ноль цзяо ноль фыней')
    def test_651_000_000_000z_04_only_number(self):
        result = converter(651_000_000_000.01, only_rubles=True, only_number=True, currency="CNY")
        self.assertEqual(result, 'шестьсот пятьдесят один миллиард')
    def test_651_000_000_000z_04_only_numder(self):
        result = converter(651_000_000_000.01, only_rubles=True, currency="CNY")
        self.assertEqual(result, 'шестьсот пятьдесят один миллиард юаней')
    def test_651_000_000_001z_04_only_numder(self):
        result = converter(651_000_000_001.01, only_rubles=True, currency="CNY")
        self.assertEqual(result, 'шестьсот пятьдесят один миллиард один юань')
    def test_651_000_000_001z_only_rubles_only_number(self):
        result = converter(651_000_000_001.01, only_rubles=True, only_number=True, currency="CNY")
        self.assertEqual(result, 'шестьсот пятьдесят один миллиард один')
    def test_651_000_000_001z21(self):
        result = converter(651_000_000_001.21, currency="CNY")
        self.assertEqual(result, 'шестьсот пятьдесят один миллиард один юань два цзяо один фынь')
    def test_z21(self):
        result = converter(0.21, currency="CNY")
        self.assertEqual(result, 'ноль юаней два цзяо один фынь')
    def test_1z21(self):
        result = converter(1.21, currency="CNY")
        self.assertEqual(result, 'один юань два цзяо один фынь')
    def test_1z21_only_rubles(self):
        result = converter(1.21, currency="CNY", only_rubles=True)
        self.assertEqual(result, 'один юань')
    def test_1z21_only_number(self):
        result = converter(1.21, currency="CNY", only_rubles=True, only_number=True)
        self.assertEqual(result, 'один')
    def test_12345678z24(self):
        result = converter(12345678.24, currency="CNY")
        self.assertEqual(result, 'двенадцать миллионов триста сорок пять тысяч шестьсот семьдесят восемь юаней два цзяо четыре фыня')
    def test_1z01(self):
        result = converter(1.01, currency="CNY")
        self.assertEqual(result, 'один юань ноль цзяо один фынь')
    def test_22z02(self):
        result = converter(22.02, currency="CNY")
        self.assertEqual(result, 'двадцать два юаня ноль цзяо два фыня')

if __name__ == '__main__':
    unittest.main()
