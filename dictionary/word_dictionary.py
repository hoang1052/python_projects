from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = str(input("Enter your word: "))
    if word.lower() =="":
        break
    else:
       print(dictionary.printMeanings(word))
