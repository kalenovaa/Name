country_flags = {
    'kg': {'red', 'yellow'},
    'ru': {'white', 'blue', 'red'},
    'us': {'red', 'white', 'blue'},
    'fr': {'blue', 'white', 'red'},
    'de': {'black', 'red', 'yellow'},
    'it': {'green', 'white', 'red'},
}

while True:
    user_input = input("Введите цвет(а) (или 'выход' для завершения): ").strip().lower()

    if user_input == 'выход':
        print("Выход из программы.")
        break

    colors = set(user_input.split())
    
    invalid_colors = colors - {color for sublist in country_flags.values() for color in sublist}
    if invalid_colors:
        print(f"Некорректные цвета: {', '.join(invalid_colors)}. Попробуйте снова.")
        continue

    matching_domains = []
    for domain, colors_set in country_flags.items():
        if colors.issubset(colors_set):
            matching_domains.append(domain)

    if matching_domains:
        print(f"Страны с указанными цветами: {', '.join(matching_domains)}")
    else:
        print("Нет стран с указанными цветами.")
