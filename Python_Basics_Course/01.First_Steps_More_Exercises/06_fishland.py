skumriq_price_for_kg = float(input())
caca_price_for_kg = float(input())

palamud_quantity_in_kg = float(input())
safrid_quantity_in_kg = float(input())
midi_quantity_in_kg = float(input())

midi_price = 7.50

palamud_price = skumriq_price_for_kg * 0.6
total_palamud_price = (skumriq_price_for_kg + palamud_price) * palamud_quantity_in_kg
safrid_price = caca_price_for_kg * 0.8
total_safrid_price = (caca_price_for_kg + safrid_price) * safrid_quantity_in_kg
total_midi_price = midi_quantity_in_kg * midi_price

total_price = total_palamud_price + total_safrid_price + total_midi_price
print("{:.2f}".format(total_price))




