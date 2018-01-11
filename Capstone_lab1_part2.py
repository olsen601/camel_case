# add input: done
userInput = input("Please type a sentence to convert to camel case: ")

# example = "fOnt proCESSOR and ParsER", originally used before input

userInput = userInput.lower()

userInput = userInput.title()

inputList = userInput.split(" ")

inputList[0] = inputList[0].lower()

camelCase = ""

camelCase = camelCase.join(inputList)

print('Camel case -- "'+camelCase+'"')
