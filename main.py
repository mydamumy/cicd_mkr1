def text_file_filterer():
    input_file = input("Введіть назву файлу: ").strip()
    keyword = input("Введіть ключове слово: ").strip()
    output_file = "filtered.txt"

    try:
        with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
            for line in infile:
                if keyword in line:
                    outfile.write(line)

        print(f"Фільтровані рядки збережено у {output_file}")

    except FileNotFoundError:
        print("Файл не знайдено. Перевірте правильність назви.")

text_file_filterer()
