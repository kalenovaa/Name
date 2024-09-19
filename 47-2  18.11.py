movies = {
    "Django Unchained": {
        "John": 10,
        "Jack": 9
    },
    "Troy": {}
}

while True:
    command = input("Введите команду (add_movie, add_rating, view_ratings, exit): ").strip().lower()

    if command == "exit":
        print("Выход из программы.")
        break

    elif command == "add_movie":
        movie_title = input("Введите название фильма: ").strip().title()
        if movie_title in movies:
            print("This movie already exists!")
        else:
            movies[movie_title] = {}
            print("Movie added successfully")

    elif command == "add_rating":
        movie_title = input("Введите название фильма: ").strip().title()
        if movie_title not in movies:
            print("This movie doesn't exist")
        else:
            user_name = input("Введите ваше имя: ").strip()
            if user_name in movies[movie_title]:
                print("Имя пользователя уже существует, введите другое имя.")
                continue

            rating = input("Введите вашу оценку (0-10): ").strip()
            if not rating.isdigit() or not (0 <= int(rating) <= 10):
                print("Ошибка: оценка должна быть числом от 0 до 10.")
                continue

            movies[movie_title][user_name] = int(rating)
            print(f"A rating has been added for {movie_title}: {user_name} rated it {rating}")

    elif command == "view_ratings":
        for movie, ratings in movies.items():
            if ratings:
                average_rating = sum(ratings.values()) / len(ratings)
                print(f"{movie} is rated {average_rating:.1f}")
            else:
                print(f"Rating is not yet available for {movie}")
    else:
        print("Некорректная команда, попробуйте снова.")
