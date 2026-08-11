#Find the missing words from the entered sentence.
sentence=input("Enter a sentence: ")
sentence = sentence.lower()

for ch in "abcdefghijklmnopqrstuvwxyz":
    if ch not in sentence:
        print(ch, end=" ")
