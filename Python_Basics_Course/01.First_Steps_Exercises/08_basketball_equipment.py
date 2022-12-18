annual_tax = int(input())
basketball_sneakers_price = annual_tax * 0.6
basketball_equip_price = basketball_sneakers_price * 0.8
basketball_ball_price = basketball_equip_price / 4
basketball_accessories = basketball_ball_price / 5

total_spendatures = annual_tax + basketball_sneakers_price + basketball_equip_price + basketball_ball_price \
                    + basketball_accessories
print(total_spendatures)
