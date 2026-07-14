text = "automation testing"

char_count = {}

for ch in text:
    if ch == " ":
        continue

    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

print(char_count)

text = "automation testing"

for ch in set(text):
    print(ch, ":", text.count(ch))