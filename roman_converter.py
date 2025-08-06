
def int_to_roman(num):
    # create a list of tuples
    roman_map =[
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    # build the roman numeral
    result = ""
    last_end_time = 0

    for value, symbol in roman_map:
       while num >= value:
           result += symbol
            num -= value



def roman_to_int(s):
    pass

def main():
    pass