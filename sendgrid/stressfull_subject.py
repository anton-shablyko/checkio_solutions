"""
Cases:
a. all caps
b. !!!+ at the end of line
c. 'help', 'asp', 'urgent' in Body
"""

from collections import OrderedDict


def is_stressful(subj):
    bad_guys = ['help', 'asp', 'asap', 'urgent']

    subject = subj.split()
    # case1:
    if ''.join(subject).isupper():
        return True

    # case2:
    if subj[-3] == '!!!':
        return True

    # case3:
    for word in subject:
        stage_1 = [letter.lower().replace('.', '').replace('!', '') for letter in word if letter.isalpha()]  # convert to lower case and get rid of non alpha
        clean_subj = ''.join(OrderedDict.fromkeys(stage_1))
        print(clean_subj)
        if clean_subj in bad_guys:
            return True
    return False

#is_stressful("I neeed HELP")
#print( ' ---------- ')
#is_stressful("H-E-L-P")

#print( ' ---------- ')
#is_stressful("HHHEEEEEEEEELLP")

is_stressful("We need you A.S.A.P.!!")