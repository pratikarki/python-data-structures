def functionThree():
    print('function Three')


def functionTwo():
    functionThree()
    print('function Two')


def functionOne():
    functionTwo()
    print('function One')


functionOne()
