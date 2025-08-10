def int_to_roman(num):
    if not (1 <= num <= 3999):
        raise ValueError("num must be between 1 and 3999")

    roman_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    result = ""
    for value, symbol in roman_map:
        while num >= value:
            result += symbol
            num -= value
    return result


def roman_to_int(s):
    roman_map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    s = s.strip().upper()
    total = 0

    for i in range(len(s)):
        if s[i] not in roman_map:
            raise ValueError(f"Invalid Roman numeral character: {s[i]}")
        value = roman_map[s[i]]
        if i + 1 < len(s) and value < roman_map[s[i + 1]]:
            total -= value
        else:
            total += value
    return total


def main():
    print("Integer to Roman:")
    print(f"58 -> {int_to_roman(58)}")
    print(f"1994 -> {int_to_roman(1994)}")

    print("\nRoman to Integer:")
    print(f"LVIII -> {roman_to_int('LVIII')}")
    print(f"MCMXCIV -> {roman_to_int('MCMXCIV')}")


if __name__ == "__main__":
    main()
