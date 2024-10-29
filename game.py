from heroes import Hero
import random
import time


class Game:
    """Основной класс игры"""

    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)
        self.round_number = 1

    def display_stats(self):
        """Отображение статистики обоих героев"""
        print("\nСтатистика героев:")
        print(self.player.get_stats())
        print(self.computer.get_stats())

    def player_turn(self):
        """Ход игрока"""
        while True:
            print("\nВаш ход! Выберите действие:")
            print("1. Обычная атака")
            print("2. Специальная атака (50 энергии)")
            print("3. Защита (восстанавливает 20 энергии)")
            print("4. Лечение (30 энергии)")

            try:
                choice = int(input("Введите номер действия (1-4): "))
                if choice == 1:
                    return self.player.attack(self.computer)
                elif choice == 2:
                    return self.player.special_attack(self.computer)
                elif choice == 3:
                    return self.player.defend()
                elif choice == 4:
                    return self.player.heal()
                else:
                    print("Неверный выбор. Попробуйте снова.")
            except ValueError:
                print("Пожалуйста, введите число от 1 до 4.")

    def computer_turn(self):
        """Ход компьютера"""
        # Простая ИИ логика
        if self.computer.health < 30 and self.computer.special_power >= 30:
            return self.computer.heal()
        elif self.computer.special_power >= 50 and random.random() < 0.3:
            return self.computer.special_attack(self.player)
        elif self.computer.health < 50 and random.random() < 0.4:
            return self.computer.defend()
        else:
            return self.computer.attack(self.player)

    def start(self):
        """Запуск игры"""
        print("\nИгра началась!")
        self.display_stats()

        while self.player.is_alive() and self.computer.is_alive():
            print(f"\nРаунд {self.round_number}")

            # Ход игрока
            result = self.player_turn()
            print(result)
            self.display_stats()

            if not self.computer.is_alive():
                print(f"\nПобедитель: {self.player.name}!")
                break

            # Небольшая пауза перед ходом компьютера
            print("\nХод компьютера...")
            time.sleep(1.5)

            # Ход компьютера
            result = self.computer_turn()
            print(result)
            self.display_stats()

            if not self.player.is_alive():
                print(f"\nПобедитель: {self.computer.name}!")
                break

            # Сброс удвоенной защиты в конце раунда
            self.player.defense = 5
            self.computer.defense = 5
            self.round_number += 1