mentors = ["Тимур", "Арсен", "Гулина", "Даниель"]

while True:
    print("\nкоманды:")
    print("1. добавление")
    print("2. изменения")
    print("3. удаление")
    print("0. выход + итог")

    command = input("введите команду: ").strip()

    if command == "0":
        mentors_tuple = tuple(mentors)
        print("\nитого:", mentors_tuple)
        break

    elif command == "1":
        if len(mentors) >= 10:
            print("слишком много менторов (больше 10) удалите нескольких")
            continue

        new_name = input("добавьте имя: ").strip().capitalize()
        if len(new_name) > 15:
            print("нельзя больше 15 букв")
            continue
        if new_name in mentors:
            print("это имя уже есть")
            continue

        mentors.append(new_name)
        print(f"имя '{new_name}' добавлено")

    elif command == "2":
        old_name = input("введите имя которое хотите заменить: ").strip().capitalize()
        if old_name not in mentors:
            print("имя не найдено")
            continue

        new_name = input("введите новое имя: ").strip().capitalize()
        if len(new_name) > 15:
            print("имя не должно превышать 15 букв")
            continue
        if new_name in mentors:
            print("новое имя уже есть в списке")
            continue

        index = mentors.index(old_name)
        mentors[index] = new_name
        print(f"имя '{old_name}' заменено на '{new_name}'.")

    elif command == "3":
        print("уделание по:")
        print("1. индексу")
        print("2. имени")

        delete_option = input("выберите вариант: ").strip()

        if delete_option == "1":
            try:
                index = int(input("введите индекс для удаления: "))
                if index < 0 or index >= len(mentors):
                    print("индекс не правильный")
                    continue
                removed_mentor = mentors.pop(index)
                print(f"ментор '{removed_mentor}' удален по индексу {index}.")
            except ValueError:
                print("читай условие броу")

        elif delete_option == "2":
            name_to_remove = input("введите имя для удаления: ").strip().capitalize()
            if name_to_remove not in mentors:
                print("имя не найдено в списке.")
                continue

            mentors.remove(name_to_remove)
            print(f"ментор '{name_to_remove}' удален.")

        else:
            print("неправильный выбор")

    else:
        print("неправильная команда  0, 1, 2 или 3.")

# Преобразование списка менторов в кортеж и вывод на экран
mentors_tuple = tuple(mentors)
print("\nитого:", mentors_tuple)
