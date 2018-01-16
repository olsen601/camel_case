def display_banner():
    '''Display program name in a banner'''
    msg = 'Camel Case Generator Program'
    stars = '*' * len(msg)
    print('\n', stars, '\n', msg, '\n', stars, '\n')

display_banner()
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
