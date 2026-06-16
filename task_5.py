f = open("words.txt", "r", encoding="utf-8")
words = f.read().splitlines()
f.close()

# По алфавиту
sorted_alpha = sorted(words)
f = open("sorted_alphabetically.txt", "w", encoding="utf-8")
f.write("\n".join(sorted_alpha))
f.close()

# По длине
sorted_len = sorted(words, key=len)
f = open("sorted_by_length.txt", "w", encoding="utf-8")
f.write("\n".join(sorted_len))
f.close()

# Обратный алфавит
sorted_rev = sorted(words, reverse=True)
f = open("sorted_reverse.txt", "w", encoding="utf-8")
f.write("\n".join(sorted_rev))
f.close()
