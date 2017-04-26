def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):

    ind = [i for i in range(len(powers))]
    prefix = '-' if number < 0 else ''
    def one():
        for i in reversed(ind):
            x = abs(number)//base**i
            if x > 0:
                    return i, x
        return 0, 0

    power, new_num = one()
    if decimals > 0:
        new_num = round(abs(number) / base ** power, decimals)
        format_str = ('{0}{1:.%df}{2}{3}' % decimals)
        print(format_str.format(prefix, new_num, powers[power], suffix))
        return format_str.format(prefix, new_num, powers[power], suffix)
    else:
        print('{}{}{}{}'.format(prefix, new_num, powers[power], suffix))
        return '{}{}{}{}'.format(prefix, new_num, powers[power], suffix)



#friendly_number(-150, base=100, powers=["","d","D"])
#friendly_number(-155, powers=["","d","D"], base=100, decimals=1)
friendly_number(0, decimals=3, suffix="th")

# These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert friendly_number(102) == '102', '102'
#     assert friendly_number(10240) == '10k', '10k'
#     assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
#     assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
#     assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'

