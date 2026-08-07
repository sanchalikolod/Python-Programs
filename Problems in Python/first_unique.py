#Find the first unique character in a text:

def unique(text):
    for i in range(len(text)):
        frequency=0
        for j in range(len(text)):
            if text[i]==text[j]:
                frequency=frequency+1
        if frequency==1:
            return text[i]

text=input("Enter your text: ")
result=unique(text)
print("First unique character in your text is: ",result)
        


