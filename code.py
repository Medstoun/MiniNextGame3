from functoins import get_word, random_letters, save_point, get_statistics


def main():

    score_count = 0

    words = get_word()

    user_name = input("Введите ваше имя ")


    for i in words:

        letters = random_letters(i)

        print(f"Угадайте слово: {letters}")

        user_input = input()

        if user_input == i:
            print("Верно! Вы получаете 10 очков.")
            score_count += 10
        else:
            print(f"Неверно! Верный ответ – {i}.")

    save_point(user_name, score_count)

    statistics = get_statistics()

    print(f"Всего игр сыграно: {statistics.get('len')}")
    print(f"Максимальный рекорд: {statistics.get('max')}")




main()