import random


class Hero:
    """Базовый класс для создания героев"""

    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.max_health = health  # Максимальное здоровье
        self.attack_power = attack_power
        self.defense = 5  # Базовая защита
        self.special_power = 100  # Энергия для специальных атак
        self.max_special_power = 100

    def attack(self, other):
        # Шанс критического удара 20%
        is_crit = random.random() < 0.2
        damage = self.attack_power * (2 if is_crit else 1)

        # Учет защиты противника
        final_damage = max(1, damage - other.defense)
        other.health = max(0, other.health - final_damage)

        # Восстановление энергии после атаки
        self.restore_special_power(10)

        message = f"{self.name} атакует {other.name} и наносит {final_damage} урона!"
        if is_crit:
            message += " КРИТИЧЕСКИЙ УДАР!"
        return message

    def special_attack(self, other):
        """Специальная атака, тратит энергию"""
        if self.special_power >= 50:
            self.special_power -= 50
            damage = self.attack_power * 2.5
            final_damage = max(1, damage - other.defense)
            other.health = max(0, other.health - final_damage)
            return f"{self.name} использует специальную атаку и наносит {final_damage} урона!"
        return f"{self.name} пытается использовать специальную атаку, но не хватает энергии!"

    def defend(self):
        """Усиление защиты на один ход"""
        self.defense *= 2
        self.restore_special_power(20)
        return f"{self.name} занимает оборонительную позицию!"

    def restore_special_power(self, amount):
        """Восстановление энергии"""
        self.special_power = min(self.max_special_power, self.special_power + amount)

    def heal(self):
        """Лечение героя"""
        if self.special_power >= 30:
            self.special_power -= 30
            heal_amount = 30
            self.health = min(self.max_health, self.health + heal_amount)
            return f"{self.name} восстанавливает {heal_amount} здоровья!"
        return f"{self.name} пытается исцелиться, но не хватает энергии!"

    def is_alive(self):
        return self.health > 0

    def get_stats(self):
        """Метод для получения текущей статистики героя"""
        return (f"Герой: {self.name} | "
                f"Здоровье: {self.health}/{self.max_health} | "
                f"Атака: {self.attack_power} | "
                f"Защита: {self.defense} | "
                f"Энергия: {self.special_power}/{self.max_special_power}")