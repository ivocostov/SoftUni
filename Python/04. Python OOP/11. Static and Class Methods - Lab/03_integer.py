class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):                    # види ли се че нещо в задачите започва с from да се знае че става въпрос за клас метод
        if isinstance(float_value, float):                      # с int директно се закръгля надолу или връща float // 1, т.е изчислява колко пъти подаденото
            return cls(int(float_value))                        # число се събира във float
        return "value is not a float"                           # isinstance проверява дали float_value е инстанция на даден клас в случая на float

    @classmethod
    def from_roman(cls, value: str):
        roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        from_roman_to_decimal_nums = 0

        for i in range(len(value)):
            if i != 0 and roman_numbers[value[i]] > roman_numbers[value[i - 1]]:
                from_roman_to_decimal_nums += roman_numbers[value[i]] - 2 * roman_numbers[value[i - 1]]   # ако имаме "IV", стойността на "I" от else се
            else:                                                                                         # добавя в from_roman_to_decimal_nums, защото е на индекс 0 и
                from_roman_to_decimal_nums += roman_numbers[value[i]]                                     # няма число преди него, т.е. влиза в else
        return cls(from_roman_to_decimal_nums)                                                            # след това се проверява дали цифрата от индекс 1, т.е. "V" е
                                                                                                          # по-голяма от цифрата която е от индекс 0, т.е. "I".
    @classmethod                                                                                          # Ако е, от цифрата на текущия индекс вадим цифрата, която
    def from_string(cls, value: str):                                                                     # е на предния индекс или 5 - 2*1 = 3 и този резултат се събира
        if not isinstance(value, str):                                                                    # в if-a с цифрата която е вече в брояча или 3 + 1 = 4
            return "wrong type"
        return cls(int(value))


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
