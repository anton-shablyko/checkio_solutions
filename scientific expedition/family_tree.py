def is_family(tree):
    family = list(tree[0])
    for father, son in tree[1:]:
        if father in family and son not in family:
            family.append(son)
        else:
            return False
    return True

# assertions
# is_family([["Logan", "Mike"]])  # true
#
# is_family([["Logan", "William"],  # false
#            ["Logan", "Jack"],
#            ["Mike", "Alexander"],
#            ["sebastian", "Sheer"]])
#
# is_family([["Logan", "William"],  # false
#           ["Logan", "Jack"],
#           ["Mike", "Alexander"]])
#
# is_family([["Logan","Mike"], ["Logan","Jack"], ["Mike","Logan"]])  # false