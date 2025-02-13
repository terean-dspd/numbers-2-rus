[![PyPI Downloads](https://static.pepy.tech/badge/num2rus)](https://pepy.tech/projects/num2rus)
# num2rus v 1.0.0

Небольшой python пакет для преобразования чисела в текст с учетмо множественного числа. 
A small package to convert float numbers to russian string.

## What's new
- new currencies have been added:
    - USD
    - EUR
    - CNY

## Usage

### Install package

`pip install num2rus`

### Import it

```python
 import num2rus
 num2rus.converter(1.10) # один рубль десять копеек
 num2rus.converter(651_000_000_000) # шестьсот пятьдесят один миллиард рублей ноль копеек
 num2rus.converter(
    651_000_000_000,
    zero_on=False
) # шестьсот пятьдесят один миллиард рублей
 num2rus.converter(
    651_000_000_000.01,
    only_rubles=True
) # шестьсот пятьдесят один миллиард рублей
num2rus.converter(
    651_000_000_000.01,
    currency="CNY"
) # шестьсот пятьдесят один миллиард один юань два цзяо один фынь 
```
