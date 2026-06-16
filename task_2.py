word = input().strip()

f = open("text.txt", "r", encoding="utf-8")
text = f.readlines()
f.close()

count = 0
lines_found = []

for i in range(len(text)):
    if word.lower() in text[i].lower():
        count += text[i].lower().count(word.lower())
        lines_found.append(str(i+1))

print("Found:", "Yes" if count > 0 else "No")
print("Count:", count)
print("Lines:", ", ".join(lines_found) if lines_found else "none")

f = open("search_results.txt", "w", encoding="utf-8")
f.write("Word: " + word + "\n")
f.write("Found: " + ("Yes" if count > 0 else "No") + "\n")
f.write("Count: " + str(count) + "\n")
f.write("Lines: " + (", ".join(lines_found) if lines_found else "none"))
f.close()
