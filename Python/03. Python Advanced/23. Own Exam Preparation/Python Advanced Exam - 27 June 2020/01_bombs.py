from collections import deque

bomb_effects = deque(int(x) for x in input().split(', '))
bomb_casings = deque(int(x) for x in input().split(', '))


bomb_pouch = {'Datura Bombs': 0,
              'Cherry Bombs': 0,
              'Smoke Decoy Bombs': 0
              }

bomb_pouch_is_full = False

while bomb_effects and bomb_casings and not bomb_pouch_is_full:
    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()
    result = current_effect + current_casing

    for bomb, materials in (('Datura Bombs', 40), ('Cherry Bombs', 60), ('Smoke Decoy Bombs', 120)):
        if result == materials:
            bomb_pouch[bomb] += 1
            break

    else:
        bomb_casings.append(current_casing - 5)
        bomb_effects.appendleft(current_effect)

    if all(x >= 3 for x in bomb_pouch.values()):
        bomb_pouch_is_full = True


if bomb_pouch_is_full:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")

if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")


for k, v in sorted(bomb_pouch.items()):
    print(f"{k}: {v}")


