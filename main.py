import os

def get_input_data():
    input_file = input("Введіть назву файлу: ").strip()
    keyword = input("Введіть ключове слово: ").strip()
    text_file_filterer(input_file, keyword)

def text_file_filterer(input_file, keyword):
    output_file_path = os.path.join(os.path.dirname(input_file), "filtered.txt")

    try:
        with open(input_file, "r", encoding="utf-8") as infile, open(output_file_path, "w", encoding="utf-8") as outfile:
            for line in infile:
                if keyword.lower() in line.lower():
                    outfile.write(line)

        print(f"Фільтровані рядки збережено у {output_file_path}")

    except FileNotFoundError:
        print("Файл не знайдено. Перевірте правильність назви.")

if __name__ == "__main__":
    get_input_data()