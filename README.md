![Upload Python Package](https://github.com/terean-dspd/numbers-2-rus/workflows/Upload%20Python%20Package/badge.svg)
# num2rus v 0.0.11

Небольшой python пакет для преобразования чисела в текст с учетмо множественного числа. 
A small package to convert float numbers to russian string.

## What's new
- bug fix for #8 issue

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
```
