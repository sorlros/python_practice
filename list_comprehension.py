# s = "hello"
# capitalized_s = [char.upper() for char in s]
# print(capitalized_s)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_numbers = [x for x in numbers if x % 2 == 0]
# print(even_numbers)

# nums = [3,-1,5,-2,0]
# non_nega = [0 if x < 0 else x for x in nums]
# print(non_nega)

# nums2 = [1,2,3,4,5]
# result = ["even" if num % 2 == 0 else "odd" for num in nums]
# print(result)

# words = ["hello", "world", "python", "programming"]
# upper_words = [word.upper() if len(word) > 5 else word for word in words]
# print(upper_words)

# nums2 = [10,20,30,40,50]
# halved_numbers = [num // 2 for num in nums2]
# halved_numbers2 = [num // 2 for num in range(10,60,10)] # 동일 결과
# print(halved_numbers)

# nums3 = range(1,11)
# even_squares = [num ** 2 for num in nums3 if not num % 2]
# print(even_squares)

# words = ["hi", "Python", "AI", "DeepLearning"]
# result = [word.upper() if len(word) >= 5 else word.lower() for word in words]
# print(result)

# add = lambda x, y : x + y
# print(add(1,5))

# points = [(1,3),(3,1),(5,6),(7,2)]
# points_sorted = sorted(points, key=lambda x : x[1])
# print(points_sorted)

number = [1,2,3,4,5]
print(number)
result = map(lambda x : x ** 2, number)
print(list(result))

numbers2 = [1,2,3,4,5,6,7,8,9,10]
even_number = filter(lambda x : x % 2 == 0, numbers2)
print(list(even_number))
