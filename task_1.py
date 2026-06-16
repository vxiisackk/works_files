f = open("input.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

line_count = len(lines)
word_count = 0

for line in lines:
    words = line.strip().split()
    word_count += len(words)

f = open("statistics.txt", "w", encoding="utf-8")
f.write("Lines: " + str(line_count) + "\n")
f.write("Words: " + str(word_count))
f.close()
