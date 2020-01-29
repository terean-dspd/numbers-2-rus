"""Converts `float` summ of money to Russian strings
=======================================================
"""

from typing import Tuple
from decimal import Decimal
from . converter import NUMBERS, TAILS, KOPS, RUBS


def get_rubles(dimention, value, ones, decs, hunderts):

    rubs = ""
    if dimention in ["сотня", "единица", "десятка"]:
        if value in [1, 2, 3, 4]:
            rubs = RUBS[value]
        elif decs == 1:
            rubs = RUBS[0]
        elif (hunderts > 0) and ones not in [1, 2, 3, 4]:
            rubs = RUBS[0]
        elif (hunderts > 0) and ones in [1, 2, 3, 4]:
            rubs = RUBS[ones]
        else:
            rubs = RUBS[ones]
    return rubs


def chopper(num: int) -> Tuple[str, str]:
    """Generator chops parts on a string from left to right
    =======================================================
    marks them as
    `миллиард`, `миллион`, `тысяча`, `сотня`, `единица`, `десятка`
    """
    num_str = str(num) # '20'
    while len(num_str) > 0:
        if 13 > len(num_str) >= 10:
            step = len(num_str) - 9
            yield num_str[0: step], 'миллиард'
            num_str = num_str[step:]
        if 10 > len(num_str) >= 7:
            step = len(num_str) - 6
            yield num_str[0: step], 'миллион'
            num_str = num_str[step:]
        if 7 > len(num_str) >= 4:
            step = len(num_str) - 3
            yield num_str[0: step], 'тысяча'
            num_str = num_str[step:]
        if len(num_str) == 3:
            yield num_str, 'сотня'
            break
        if len(num_str) == 1:
            yield num_str, 'единица'
            break
        if len(num_str) == 2 and num_str[0] == '1':
            yield num_str, 'десятка'
            break
        else:
            yield num_str, 'сотня'
            break


def decimal_parser(number_str: str, zero_on: bool = True) -> Tuple[str, str]:
    """
    Decimal parser
    =================
    if `zero_on` is `True` adds `ноль копеек`
    """
    tail: str = ''  # tail "копейка, копеек..."
    number_int: int = int(number_str)
    string: str = ""
    ones: int = int(number_str[-1])
    decs: int = int(number_str[-2])
    if 3 <= number_int and number_int <= 19:  # if number in 3 .. 19 get it
        string += " " + NUMBERS["додвадцати"][number_int]
    if number_int in [1, 2]:  # special case for Russian
        string += " " + NUMBERS["додвадцати"][decs*10+ones][1]
    if number_int >= 20:
        string += " " + NUMBERS["десятки"][decs*10]
        if ones > 0 and ones in [1, 2]:
            string += " " + NUMBERS["додвадцати"][ones][1]
        elif ones > 0:
            string += " " + NUMBERS["додвадцати"][ones]
    if number_int in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        tail = KOPS[number_int]
    elif decs == 1:
        tail = KOPS[0]
    elif decs > 1 and ones not in [1, 2, 3, 4]:
        tail = KOPS[0]
    elif decs > 1 and ones in [1, 2, 3, 4]:
        tail = KOPS[ones]
    if zero_on and not string and not tail:
        string = NUMBERS["додвадцати"][0]
        tail = KOPS[0]

    return string, tail


def main_parser(number_str: str, dimention: str) -> Tuple[str, str, str]:
    """
    Integer parser
    =================
    """
    string = ""  # result
    tl = ""  # teil: миллион, тысяча...
    rubs = ""  # rubles ending - "рублей, рубля"
    number_int = int(number_str)
    ones = int(number_str[-1])
    hunderts = 0
    decs = 0
    length = len(number_str)
    if dimention == "единица":
        if number_int in [1, 2]:
            string = NUMBERS["додвадцати"][ones][0]
        else:
            string = NUMBERS["додвадцати"][ones]

    if dimention == "десятка":
        string = NUMBERS["додвадцати"][number_int]

    if length >= 2:
        decs = int(number_str[-2])

    if length == 3:
        hunderts = int(number_str[-3])

    if hunderts >= 1:
        string += NUMBERS["сотни"][hunderts * 100]
        tl = TAILS[dimention]['other']

    if decs == 0 and ones > 0 and dimention != "единица":  # 1 - 9
        if dimention in ['тысяча'] and ones in [1, 2]:
            string += " " + NUMBERS["додвадцати"][decs*10+ones][1]
        elif ones in [1, 2]:
            string += " " + NUMBERS["додвадцати"][decs*10+ones][0]
        else:
            string += " " + NUMBERS["додвадцати"][decs*10+ones]
        tl = TAILS[dimention]['додвадцати'][decs*10+ones]
    elif decs == 1 and dimention != "десятка":  # 10 - 19
        string += " " + NUMBERS["додвадцати"][decs*10+ones]
        tl = TAILS[dimention]['додвадцати'][decs*10+ones]
    elif decs > 1:
        string += " " + NUMBERS["десятки"][decs*10]
        tl = TAILS[dimention]['other']
        if ones in [1, 2]:
            string += " " + NUMBERS["додвадцати"][ones][0]
        elif ones > 2:
            string += " " + NUMBERS["додвадцати"][ones]
            tl = TAILS[dimention]['додвадцати'][ones]
    rubs = get_rubles(dimention, number_int, ones, decs, hunderts)
    return string, tl, rubs


def converter(number: float, zero_on: bool = True) -> str:
    if not isinstance(number, float):
        try:
            number = float(number)
        except ValueError:
            return None
    decimal: Decimal = Decimal(str(number))
    integet_part: int = int(decimal)
    dec_str = "{0:.2f}".format(decimal - integet_part)
    decimal_part: str = dec_str.split('.')[1]
    result = ''
    for number, size in chopper(integet_part):
        string, tl, rub = main_parser(number, size)
        result += string + tl + ' '
    main_part = result.strip()
    decimal_part, kops = decimal_parser(decimal_part, zero_on)

    return " ".join([main_part, rub, decimal_part.strip(), kops]).strip()


if __name__ == "__main__":
    # num = input()
    converter(20)
