from words import words
import random


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word

def hangman_game():


    HANGMAN = (
        """6 попыток  """,
        """5 попыток """,
        """4 попытки """,
        """3 попытки """,
        """2 попытки """,
        """1 попытка """,
        """Тебя повесили!"""
    )

    max_wrong = len(HANGMAN) - 1
    word = get_valid_word(words) # Слово, которое нужно угадать
    so_far = "_" * len(word)  # Одна черточка для каждой буквы в слове, которое нужно угадать
    wrong = 0  # Количество неверных предположений, сделанных игроком
    used = []  # Буквы уже угаданы

    while wrong < max_wrong and so_far != word:
        print(HANGMAN[wrong])  # Вывод висельника по индексу
        print("\nВы использовали следующие буквы:\n", used)
        print("\nНа данный момент слово выглядит так:\n", so_far)

        guess = input("\n\nВведите свое предположение: ")  # Пользователь вводит предполагаемую букву

        while guess in used:
            print("Вы уже вводили букву", guess)  # Если буква уже вводилась ранее
            guess = input("Введите свое предположение: ")  # Пользователь вводит предполагаемую букву

        used.append(guess)  # В список использованных букв добавляется введённая буква

        if guess in word:  # Если введённая буква есть в загаданном слове
            print("\nДа!", guess, "есть в слове!")
            new = ""
            for i in range(len(word)):  # В цикле добавляем найденную букву в нужное место
                if guess == word[i]:
                    new += guess
                else:
                    new += so_far[i]
            so_far = new

        else:
            print(
                "\nИзвините, буквы \"" + guess + "\" нет в слове.")  # Если буквы нет, то выводим соответствующее сообщение
            wrong += 1

    if wrong == max_wrong:  # Если игрок превысил кол-во ошибок, то его повесили
        print(HANGMAN[wrong])

    else:  # Если кол-во ошибок не превышено, то игрок выиграл
        print("\nВы угадали слово!")

    print("\nЗагаданное слово было :" , word)




if __name__ == '__main__':
    hangman_game()