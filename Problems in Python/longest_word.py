#Find the longest word in a given sentence.

text=input("Enter a sentence:")
word=""
longest=""
for ch in text:
    if ch!=" ":
        word=word+ch
    else:
        if len(word)>len(longest):
            longest=word
            word=""
        
print("Your sentence is: ",text)
print("Longest word in sentence is: ",longest)
