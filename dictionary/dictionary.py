import json

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    else:
        print("You have entered wrong word please check it again")
word = input("Enter word you want to search for: ")
output = translate(word)
print(output)