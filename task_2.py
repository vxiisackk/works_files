word = input().strip()

f = open("text.txt", "r", encoding="utf-8")
text = f.readlines()
f.close()

count = 0
lines_found = []

for i in range(len(text)):
    if word in text[i]:
        count += text[i].count(word)
        lines_found.append(str(i+1))

print("Найдено:", "Да" if count > 0 else "Нет")
print("Количество:", count)
print("Строки:", ", ".join(lines_found) if lines_found else "нет")

f = open("search_results.txt", "w", encoding="utf-8")
f.write("Слово: " + word + "\n")
f.write("Найдено: " + ("Да" if count > 0 else "Нет") + "\n")
f.write("Количество: " + str(count) + "\n")
f.write("Строки: " + (", ".join(lines_found) if lines_found else "нет"))
f.close()
