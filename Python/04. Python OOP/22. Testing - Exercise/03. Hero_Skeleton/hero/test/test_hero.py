from unittest import TestCase, main
from MainProblem.project import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero('Ivo', 1, 100, 100)
        self.enemy = Hero('Enemy', 1, 50, 50)

    def test_initialization(self):
        self.assertEqual(self.hero.username, 'Ivo')
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 100)

    def test_battle_raise_exception(self):
        with self.assertRaises(Exception) as error:
            self.enemy.battle(self.enemy)

        self.assertEqual(str(error.exception), "You cannot fight yourself")

    def test_battle_when_hero_zero_health_raises_value_error(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as error:
            self.hero.battle(self.enemy)

        self.assertEqual(str(error.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_when_enemy_zero_health_raises_value_error(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as error:
            self.hero.battle(self.enemy)

        self.assertEqual(str(error.exception), "You cannot fight Enemy. He needs to rest")

    def test_health_removal_and_damage_dealing(self):
        self.hero.health = self.enemy.health
        self.hero.damage = self.enemy.damage

        result = self.hero.battle(self.enemy)

        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.hero.health)
        self.assertEqual('Draw', result)

    def test_enemy_loose_expect_own_stats_improved(self):
        result = self.hero.battle(self.enemy)  # тества се победа на героя

        self.assertEqual(2, self.hero.level)  #  lvl + 1
        self.assertEqual(55, self.hero.health)  # тук е 50 понеже в оригиналния код enemy прави 50 dmg и сваля 50 HP
        self.assertEqual(105, self.hero.damage)  # dmg + 1
        self.assertEqual('You win', result)

    def test_hero_loose_expect_enemy_stats_improved(self):
        self.hero, self.enemy = self.enemy, self.hero  # разменят се статсовете на героите за да може да се тества загуба от героя
        result = self.hero.battle(self.enemy)

        self.assertEqual(2, self.enemy.level)  # lvl + 1
        self.assertEqual(55, self.enemy.health)  # тук е 50 понеже в оригиналния код enemy прави 50 dmg и сваля 50 HP
        self.assertEqual(105, self.enemy.damage)  # dmg + 1
        self.assertEqual('You lose', result)

    def test_correct__str__(self):
        self.assertEqual(f"Hero Ivo: 1 lvl\n"
                         f"Health: 100\n"
                         f"Damage: 100\n",
                         str(self.hero)
                         )



if __name__ == '__main__':
    main()
