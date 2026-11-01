import string


def get_word_frequencies(text):
    # Видаляємо пунктуацію та переводимо текст у нижній регістр
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = cleaned_text.split()

    # Створюємо словник частот
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


# Тестовий текст для перевірки
sample_text = """
Слово, слово, слово, слово. 
Код код код код код. 
Тест тест.
"""

# Отримуємо словник з частотою слів
word_counts = get_word_frequencies(sample_text)

# Створюємо список слів, які зустрічаються більше 3 разів
frequent_words = [word for word, count in word_counts.items() if count > 3]

# Виводимо результати
print("Словник частот слів:")
print(word_counts)
print("\nСлова, що зустрічаються більше 3 разів:")
print(frequent_words)

