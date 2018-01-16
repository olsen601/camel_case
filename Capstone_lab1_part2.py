def display_banner():
    '''Display program name in a banner'''
    msg = 'Camel Case Generator Program'
    stars = '*' * len(msg)
    print('\n', stars, '\n', msg, '\n', stars, '\n')

def instructions():
    '''Display instructions'''
    msg = 'Please enter a sentence to convert to camel case'
    print('\n', msg, '\n')

display_banner()

instructions()

# add input: done
userInput = input(": ")

# example = "fOnt proCESSOR and ParsER", originally used before input

userInput = userInput.lower()

userInput = userInput.title()

inputList = userInput.split(" ")

inputList[0] = inputList[0].lower()

camelCase = ""

camelCase = camelCase.join(inputList)

print('Camel case -- "'+camelCase+'"')
