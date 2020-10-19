def repeated(L):
    '''Reduce the input list to a list of all repeated integers in the list.'''
    return [item for item in list(set(L)) if L.count(item) > 1]

def print_result(L, name):
    '''Print the output for one list.'''
    output = repeated(L)
    print ('%s count = %i (for %s)' % (name, len(output), output))

list_a = [1,2,3,3,1,2,3,3]
list_b = [67, 4, 67, 4, 67, 4, 67, 4, 2, 9, 0]
list_c = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2,
    3, 4, 5, 6, 7, 8, 9, 0, 23, 18, 10
]

print_result(list_a, 'list_a')
print_result(list_b, 'list_b')
print_result(list_c, 'list_c')