words = ["a", "e", "i", "o", "u"]
vowel = input("Type a sentence: ")
for i in vowel:
    if i not in "aeiou":
        print(i)
    if i == "aeiou":
        continue
