import string

# Функція для сортування та видалення дублікатів
def sort_and_unique(words):
    return sorted(set(words), key=lambda s: s.lower())

def read_first_sentence(file_path):
    try:
        # Читання файлу
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Знаходимо перше речення (враховуючи також ? та !)
        sentence_end = min([text.find(c) for c in '.!?'] + [len(text)])
        first_sentence = text[:sentence_end+1].strip()

        print("Перше речення: ", first_sentence)

        # Видаляємо пунктуацію
        text_without_punctuation = text.translate(str.maketrans('', '', string.punctuation))

        # Розбиваємо текст на слова
        words = text_without_punctuation.split()

        # Визначення українських та англійських слів
        ukrainian_words = [word for word in words if any('а' <= char <= 'я' or 'А' <= char <= 'Я' for char in word)]
        english_words = [word for word in words if all('a' <= char.lower() <= 'z' for char in word)]

        # Сортування і видалення дублікатів
        ukrainian_words_sorted = sort_and_unique(ukrainian_words)
        english_words_sorted = sort_and_unique(english_words)

        # Виведення результатів
        print("Українські слова (відсортовані, унікальні): ", ukrainian_words_sorted)
        print("Англійські слова (відсортовані, унікальні): ", english_words_sorted)
        print("Загальна кількість слів:", len(words))  # Загальна кількість слів
        print("Кількість унікальних слів:", len(set(words)))  # Кількість унікальних слів

    except FileNotFoundError:
        print(f"Помилка: файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

# Виклик функції
file_path = "text.txt"
read_first_sentence(file_path)
