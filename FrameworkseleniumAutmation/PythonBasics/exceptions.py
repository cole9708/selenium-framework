ItemInCart = 2


if ItemInCart !=2:
    raise Exception('wrong amount of items in cart')

try:
    with open('log.txt') as logfile:
        logfile.read()
except Exception as e:
    print(' failure due to the file not exisiting')
    print(e)