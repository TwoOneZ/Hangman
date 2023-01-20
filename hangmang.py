from words import words
import random


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word


def hangman_game():
    max_attempts = 6
    word = get_valid_word(words)  # Слово, которое нужно угадать
    Length_word = "_" * len(word)  # Одна черточка для каждой буквы в слове, которое нужно угадать
    fails = 0  # Количество неверных предположений, сделанных игроком
    used = []  # Буквы уже угаданы

    while fails < max_attempts and Length_word != word:

        print(f"\nВы использовали следующие буквы: {used} \nНа данный момент слово выглядит так:\n {Length_word}")

        guess = input("\nВведите свое предположение: ")  # Пользователь вводит предполагаемую букву

        while guess in used:
            print(f"Вы уже вводили букву {guess}")  # Если буква уже вводилась ранее
            guess = input("Введите свое предположение: ")  # Пользователь вводит предполагаемую букву

        used.append(guess)  # В список использованных букв добавляется введённая буква

        if guess in word:  # Если введённая буква есть в загаданном слове
            print(f"\n{guess} есть в слове!")
            new = ""
            for i in range(len(word)):  # В цикле добавляем найденную букву в нужное место
                if guess == word[i]:
                    new += guess
                else:
                    new += Length_word[i]
            Length_word = new

        else:
            fails += 1
            print(f"\nИзвините, буквы {guess} нет в слове.\nУ вас осталось {max_attempts - fails} попыток")  # Если буквы нет, то выводим соответствующее сообщение

    if fails == 6:  # Если игрок превысил кол-во ошибок, то его повесили
        print("\nВы проиграли")

    else:  # Если кол-во ошибок не превышено, то игрок выиграл
        print("\nВы угадали слово!")

    print(f"\nЗагаданное слово было : {word}")


if __name__ == '__main__':
    hangman_game()
