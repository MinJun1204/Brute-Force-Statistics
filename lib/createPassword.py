import random, string

def createPassword(opt, digit):
    if opt == 'N':
        pool = string.digits
    elif opt == 'AL':
        pool = string.ascii_lowercase
    elif opt == 'NALU':
        pool = string.digits + string.ascii_lowercase + string.ascii_uppercase
    elif opt == 'NALUS':
        pool = string.printable
    else:
        print('Option Error')
        return
    
    result = ''

    for i in range(digit):
        result += random.choice(pool)

    return result