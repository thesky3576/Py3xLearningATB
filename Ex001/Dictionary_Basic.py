my_dict = {'a': 1, 'b': 2, 'c': 3}
for k,v in my_dict.items():
     if k == 'b':
         print(f"key b having value {my_dict.get('b')} found")
op ='b'in my_dict
print(op)
