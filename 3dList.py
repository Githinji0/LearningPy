import pprint

printer = pprint.PrettyPrinter()

lst = []

for a in range(5):
    list1 = []
    for b in range(5):
        list2 = []
        for number in range(5):
            list2.append(number)
        list1.append(list2)
    lst.append(list1)
printer.pprint(lst)

# __alt__

lst2 = [[[number for number in range(5)] for _ in range(5)] for _ in range(5)]
printer.pprint(lst2)
