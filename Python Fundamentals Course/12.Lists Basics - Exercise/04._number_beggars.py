money = input().split(", ")
count_of_beggars = int(input())

beggars_sums = []           # запазва сумите на всеки просяк
beggar_starting_index = 0   # брояч на индексите запазени в numbers, тъй като всеки следващ просяк трябва да започва да взема пари от следващия по ред индекс
money_as_digits = []

for current_number in money:
    money_as_digits.append(int(current_number))

while beggar_starting_index < count_of_beggars:
    current_beggar_sum = 0                                                           # брояч на текущата сума на текущия просяк, като при всеки нов просяк се занулява
    for current_index in range(beggar_starting_index, len(money), count_of_beggars): # проверка на индексите на просяците:
        current_beggar_sum += money_as_digits[current_index]                         # цикълът започва от стартовия индекс на просяка
    beggars_sums.append(current_beggar_sum)                                          # минава през целия списък на money
    beggar_starting_index += 1                                                       # със стъпка бройката на просяците
                                                                                     # т.е ако са двама просяка, първият взима
print(beggars_sums)                                                                  # от индекс 1, 3 и т.н; вторият взима от индекс 2, 4 и т.н.