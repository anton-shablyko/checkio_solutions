def checkio(number):
    x = '{0:b}'.format(number)
    return(str(x).count('1'))

checkio(4)