#List
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list          # Prints complete list
print list[0]       # Prints first element of the list
print list[1:3]     # Prints elements starting from 2nd till 3rd
print list[2:]      # Prints elements starting from 3rd element
print tinylist * 2  # Prints list two times
print list + tinylist # Prints concatenated lists


Dict=dict(first="1",secont=2)
print(Dict.get("secont"))

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print(tinydict.get("name"))

for index in list:
    print(index)