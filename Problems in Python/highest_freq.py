#Find character with highest frequency:

def highest_frequency(text):
    max_char=""
    max_count=0
    for i in range(len(text)):
        frequency=0
        for j in range(len(text)):
            if text[i]==text[j]:
                frequency+=1
            if frequency>max_count:
                max_count=frequency
                max_char=text[i]
    print("Highest frequency character: ",max_char)
    print("Frequency of above character: ",max_count)

text=input("Enter your text: ")
highest_frequency(text)
