lst = [1,2,3,4,5]
result = map(lambda x : x + 10, lst)
print(list(result))

str_lst = ["apple", "banana", "cherry"]
result = map(lambda x : x.upper(), str_lst)
print(list(result))

str_lst = ["lion", "cat", "door", "hi", "python"]
result = filter(lambda x: len(x) == 4, str_lst)
print(list(result))

str_lst = ["banana", "apple", "kiwi"]
result = sorted(str_lst, key = lambda x: len(x), reverse=True)
print(result)