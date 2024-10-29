from game import Game


def display_welcome():
    """Отображение приветственного сообщения"""
    print("=" * 50)
    print("Добро пожаловать в игру 'Битва Героев'!")
    print("=" * 50)
    print("\nПравила игры:")
    print("1. У каждого героя есть здоровье (100) и сила атаки (20)")
    print("2. Игроки ходят по очереди")
    print("3. Побеждает тот, кто первым уничтожит противника")
    print("\n")


def main():
    display_welcome()
    while True:
        player_name = input("Введите имя вашего героя: ")
        if player_name.strip():  # Проверка на пустое имя
            break
        print("Имя не может быть пустым! Попробуйте снова.")

    game = Game(player_name)
    game.start()

    # Предложение сыграть снова
    while True:
        play_again = input("\nХотите сыграть снова? (да/нет): ").lower()
        if play_again in ['да', 'нет']:
            if play_again == 'да':
                main()
            else:
                print("Спасибо за игру! До свидания!")
            break
        print("Пожалуйста, введите 'да' или 'нет'")


if __name__ == "__main__":
    main()