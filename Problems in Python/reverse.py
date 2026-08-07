#Reverse every word of a sentence without changing the order of words.

text=input("Enter your text: ")
word=""
result=""
for ch in text:
    if ch!=" ":
        word=ch+word
    else:
        result=result+word+" "
        word=""
result=result+word

print("Reversed words text: ",result)
