#Counting of words:

text=input("Enter text: ")
count=1
for ch in text:
    if ch==" ":
        count=count+1

print("No. of words in sentence: ",count)
