def initial_party(party_members):
    for current_hero in range(party_members):
        hero_stats = input().split()
        hero_name, hero_hp, hero_mp = hero_stats[0], int(hero_stats[1]), int(hero_stats[2])
        hero_dictionary[hero_name] = [hero_hp, hero_mp]



def cast_spell(hero_name, mp_needed, spell_name):
    if hero_name in hero_dictionary.keys():
        mp_max = 200
        if mp_needed <= int(hero_dictionary[hero_name][-1]) <= mp_max:
            hero_dictionary[hero_name][-1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {hero_dictionary[hero_name][-1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")


def take_damage(hero_name, damage, attacker):
    if hero_name in hero_dictionary.keys():
        hp_max = 100
        if 0 < int(hero_dictionary[hero_name][0]) <= hp_max:
            hero_dictionary[hero_name][0] -= damage
            if hero_dictionary[hero_name][0] > 0:
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hero_dictionary[hero_name][0]} HP left!")
            else:
                del hero_dictionary[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")


def recharge(hero_name, mp_amount):
    if hero_name in hero_dictionary.keys():
        mp_max = 200
        mp_to_be_recharged = abs(mp_max - hero_dictionary[hero_name][-1])
        if int(hero_dictionary[hero_name][-1]) + mp_amount <= mp_max:
            hero_dictionary[hero_name][-1] += mp_amount
            print(f"{hero_name} recharged for {mp_amount} MP!")
        else:
            hero_dictionary[hero_name][-1] = 200
            print(f"{hero_name} recharged for {mp_to_be_recharged} MP!")


def heal(hero_name, hp_amount):
    if hero_name in hero_dictionary.keys():
        hp_max = 100
        hp_to_be_recharged = abs(hp_max - hero_dictionary[hero_name][0])
        if int(hero_dictionary[hero_name][0]) + hp_amount <= hp_max:
            hero_dictionary[hero_name][0] += hp_amount
            print(f"{hero_name} healed for {hp_amount} HP!")
        else:
            hero_dictionary[hero_name][0] = 100
            print(f"{hero_name} healed for {hp_to_be_recharged} HP!")


def main_function(party_members):
    initial_party(party_members)

    while True:
        hero_action = input().split(" - ")
        if hero_action[0] == 'End':
            break

        action = hero_action[0]
        if action == 'CastSpell':
            hero_name = hero_action[1]
            mp_needed = int(hero_action[2])
            spell_name = hero_action[3]
            cast_spell(hero_name, mp_needed, spell_name)
        elif action == 'TakeDamage':
            hero_name = hero_action[1]
            damage = int(hero_action[2])
            attacker = hero_action[3]
            take_damage(hero_name, damage, attacker)
        elif action == 'Recharge':
            hero_name = hero_action[1]
            mp_amount = int(hero_action[2])
            recharge(hero_name, mp_amount)
        elif action == 'Heal':
            hero_name = hero_action[1]
            hp_amount = int(hero_action[2])
            heal(hero_name, hp_amount)

    for hero, stats in hero_dictionary.items():
        print(f"{hero}")
        print(f" HP: {stats[0]}")
        print(f" MP: {stats[-1]}")


number_of_heroes = int(input())
hero_dictionary = {}
main_function(number_of_heroes)