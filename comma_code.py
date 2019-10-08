def comma_code(listparameter):
    newString = ''
    for i in range(len(listparameter)):
        if i == len(listparameter)-1:
            newString += 'and ' + listparameter[i]
        else:
            newString += listparameter[i] + ', '
    print(newString)


spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs']
comma_code(spam)
