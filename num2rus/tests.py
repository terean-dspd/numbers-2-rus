import unittest

from . main import converter


class Testconverter(unittest.TestCase):
    # def test_0(self):
    #     result = converter(1)
    #     self.assertEqual(result, 'один')
    def test_1(self):
        result = converter(1, zero_on=False)
        self.assertEqual(result, 'один рубль')

    def test_2(self):
        result = converter(2, zero_on=False)
        self.assertEqual(result, 'два рубля')

    def test_3(self):
        result = converter(3, zero_on=False)
        self.assertEqual(result, 'три рубля')

    def test_7(self):
        result = converter(7, zero_on=False)
        self.assertEqual(result, 'семь рублей')

    def test_10(self):
        result = converter(10, zero_on=False)
        self.assertEqual(result, 'десять рублей')

    def test_20(self):
        result = converter(20, zero_on=False)
        self.assertEqual(result, 'двадцать рублей')

    def test_21(self):
        result = converter(21, zero_on=False)
        self.assertEqual(result, 'двадцать один рубль')

    def test_25(self):
        result = converter(25, zero_on=False)
        self.assertEqual(result, 'двадцать пять рублей')

    def test_30(self):
        result = converter(30, zero_on=False)
        self.assertEqual(result, 'тридцать рублей')

    def test_33(self):
        result = converter(33, zero_on=False)
        self.assertEqual(result, 'тридцать три рубля')

    def test_43(self):
        result = converter(43, zero_on=False)
        self.assertEqual(result, 'сорок три рубля')

    def test_50(self):
        result = converter(50, zero_on=False)
        self.assertEqual(result, 'пятьдесят рублей')
    def test_75(self):
        result = converter(75, zero_on=False)
        self.assertEqual(result, 'семьдесят пять рублей')

    def test_90(self):
        result = converter(90, zero_on=False)
        self.assertEqual(result, 'девяносто рублей')
    def test_99(self):
        result = converter(99, zero_on=False)
        self.assertEqual(result, 'девяносто девять рублей')
    def test_100(self):
        result = converter(100, zero_on=False)
        self.assertEqual(result, 'сто рублей')

    def test_101(self):
        result = converter(101, zero_on=False)
        self.assertEqual(result, 'сто один рубль')

    def test_111(self):
        result = converter(111, zero_on=False)
        self.assertEqual(result, 'сто одинадцать рублей')

    def test_115(self):
        result = converter(115, zero_on=False)
        self.assertEqual(result, 'сто пятнадцать рублей')

    def test_120(self):
        result = converter(120, zero_on=False)
        self.assertEqual(result, 'сто двадцать рублей')

    def test_1120(self):
        result = converter(1120, zero_on=False)
        self.assertEqual(result, 'одна тысяча сто двадцать рублей')

    def test_5120(self):
        result = converter(5120, zero_on=False)
        self.assertEqual(result, 'пять тысяч сто двадцать рублей')

    def test_11100(self):
        result = converter(11100, zero_on=False)
        self.assertEqual(result, 'одинадцать тысяч сто рублей')

    def test_34102(self):
        result = converter(34102, zero_on=False)
        self.assertEqual(result, 'тридцать четыре тысячи сто два рубля')

    def test_34103(self):
        result = converter(34103, zero_on=False)
        self.assertEqual(result, 'тридцать четыре тысячи сто три рубля')

    def test_34000(self):
        result = converter(34000, zero_on=False)
        self.assertEqual(result, 'тридцать четыре тысячи рублей')

    def test_100000(self):
        result = converter(100_000, zero_on=False)
        self.assertEqual(result, 'сто тысяч рублей')

    def test_100100(self):
        result = converter(100_100, zero_on=False)
        self.assertEqual(result, 'сто тысяч сто рублей')

    def test_100101(self):
        result = converter(100_101, zero_on=False)
        self.assertEqual(result, 'сто тысяч сто один рубль')

    def test_100102(self):
        result = converter(100_102, zero_on=False)
        self.assertEqual(result, 'сто тысяч сто два рубля')

    def test_101102(self):
        result = converter(101_102, zero_on=False)
        self.assertEqual(result, 'сто одна тысяча сто два рубля')

    def test_1_100_101(self):
        result = converter(1_100_101, zero_on=False)
        self.assertEqual(result, 'один миллион сто тысяч сто один рубль')

    def test_1_100_102(self):
        result = converter(1_100_102, zero_on=False)
        self.assertEqual(result, 'один миллион сто тысяч сто два рубля')

    def test_1_101_102(self):
        result = converter(1_101_102, zero_on=False)
        self.assertEqual(result, 'один миллион сто одна тысяча сто два рубля')

    def test_100_101_102(self):
        result = converter(100_101_102, zero_on=False)
        self.assertEqual(result, 'сто миллионов сто одна тысяча сто два рубля')

    def test_101_101_102(self):
        result = converter(101_101_102, zero_on=False)
        self.assertEqual(
            result, 'сто один миллион сто одна тысяча сто два рубля')


class TestconverterZeroKops(unittest.TestCase):
    # def test_0(self):
    #     result = converter(1)
    #     self.assertEqual(result, 'один')
    def test_1(self):
        result = converter(1)
        self.assertEqual(result, 'один рубль ноль копеек')

    def test_2(self):
        result = converter(2)
        self.assertEqual(result, 'два рубля ноль копеек')

    def test_3(self):
        result = converter(3)
        self.assertEqual(result, 'три рубля ноль копеек')

    def test_7(self):
        result = converter(7)
        self.assertEqual(result, 'семь рублей ноль копеек')

    def test_10(self):
        result = converter(10)
        self.assertEqual(result, 'десять рублей ноль копеек')

    def test_100(self):
        result = converter(100)
        self.assertEqual(result, 'сто рублей ноль копеек')

    def test_101(self):
        result = converter(101)
        self.assertEqual(result, 'сто один рубль ноль копеек')

    def test_111(self):
        result = converter(111)
        self.assertEqual(result, 'сто одинадцать рублей ноль копеек')

    def test_115(self):
        result = converter(115)
        self.assertEqual(result, 'сто пятнадцать рублей ноль копеек')

    def test_120(self):
        result = converter(120)
        self.assertEqual(result, 'сто двадцать рублей ноль копеек')

    def test_1120(self):
        result = converter(1120)
        self.assertEqual(result, 'одна тысяча сто двадцать рублей ноль копеек')

    def test_5120(self):
        result = converter(5120)
        self.assertEqual(result, 'пять тысяч сто двадцать рублей ноль копеек')

    def test_11100(self):
        result = converter(11100)
        self.assertEqual(result, 'одинадцать тысяч сто рублей ноль копеек')

    def test_34102(self):
        result = converter(34102)
        self.assertEqual(
            result, 'тридцать четыре тысячи сто два рубля ноль копеек')

    def test_34103(self):
        result = converter(34103)
        self.assertEqual(
            result, 'тридцать четыре тысячи сто три рубля ноль копеек')

    def test_34000(self):
        result = converter(34000)
        self.assertEqual(result, 'тридцать четыре тысячи рублей ноль копеек')

    def test_100000(self):
        result = converter(100_000)
        self.assertEqual(result, 'сто тысяч рублей ноль копеек')

    def test_100100(self):
        result = converter(100_100)
        self.assertEqual(result, 'сто тысяч сто рублей ноль копеек')

    def test_100101(self):
        result = converter(100_101)
        self.assertEqual(result, 'сто тысяч сто один рубль ноль копеек')

    def test_100102(self):
        result = converter(100_102)
        self.assertEqual(result, 'сто тысяч сто два рубля ноль копеек')

    def test_101102(self):
        result = converter(101_102)
        self.assertEqual(result, 'сто одна тысяча сто два рубля ноль копеек')

    def test_1_100_101(self):
        result = converter(1_100_101)
        self.assertEqual(
            result, 'один миллион сто тысяч сто один рубль ноль копеек')

    def test_1_100_102(self):
        result = converter(1_100_102)
        self.assertEqual(
            result, 'один миллион сто тысяч сто два рубля ноль копеек')

    def test_1_101_102(self):
        result = converter(1_101_102)
        self.assertEqual(
            result, 'один миллион сто одна тысяча сто два рубля ноль копеек')

    def test_100_101_102(self):
        result = converter(100_101_102)
        self.assertEqual(
            result, 'сто миллионов сто одна тысяча сто два рубля ноль копеек')

    def test_101_101_102(self):
        result = converter(101_101_102)
        self.assertEqual(
            result,
            'сто один миллион сто одна тысяча сто два рубля ноль копеек')


class TestconverterNonZeroKops(unittest.TestCase):
    # def test_0(self):
    #     result = converter(1)
    #     self.assertEqual(result, 'один')
    def test_1_z_10(self):
        result = converter(1.10)
        self.assertEqual(result, 'один рубль десять копеек')

    def test_1_z_131_40(self):
        result = converter(131.40)
        self.assertEqual(result, 'сто тридцать один рубль сорок копеек')

    def test_1_z_123_40(self):
        result = converter(123.40)
        self.assertEqual(result, 'сто двадцать три рубля сорок копеек')


    def test_1_z_133_41(self):
        result = converter(133.41)
        self.assertEqual(result, 'сто тридцать три рубля сорок одна копейка')

    def test_1_z_01(self):
        result = converter(1.01)
        self.assertEqual(result, 'один рубль одна копейка')

    def test_2_z_02(self):
        result = converter(2.02)
        self.assertEqual(result, 'два рубля две копейки')

    def test_3_z_07(self):
        result = converter(3.07)
        self.assertEqual(result, 'три рубля семь копеек')

    def test_3_z_08(self):
        result = converter(3.08)
        self.assertEqual(result, 'три рубля восемь копеек')

    def test_7_z_11(self):
        result = converter(7.11)
        self.assertEqual(result, 'семь рублей одинадцать копеек')

    def test_10_z_21(self):
        result = converter(10.21)
        self.assertEqual(result, 'десять рублей двадцать одна копейка')


if __name__ == '__main__':
    unittest.main()
