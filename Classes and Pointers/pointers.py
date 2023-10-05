dict1 = { 'value': 11 }
dict2 = dict1

print('dict1', dict1, id(dict1))
print('dict2', dict2, id(dict2))

dict2['value'] = 10

print('dict1', dict1, id(dict1))
print('dict2', dict2, id(dict2))