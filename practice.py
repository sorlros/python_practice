# # print('I eat %d apples' %3)
# # print('I eat %s apples' %'five')
# # number = 3
# # print('I eat %d apples' %number)
# # print('I eat %d apples and %s' %(3, 'a banana'))
# # print('Error is %d%%' %85)

# # a = ["a", "b", "c", "d"]
# # # a.split(":")

# # first_int = int(input("첫번 째 숫자를 입력하세여"))
# # second_int = int(input("두번 째 숫자를 입력하세여"))

# # quotient = first_int // second_int
# # remainder = first_int % second_int

# # print(f"몫 값: {quotient}")
# # print(f"나머지 값: {remainder}")

# # # 아래 문자열 s에서 소문자 p의 위치를 출력하는 프로그램을 작성하세요.
# # s = "Python programming"

# # bb = s.index("p")
# # print(f"p의 index 위치는: {bb}")

# # # 사용자로부터 특정 문자를 입력받아, 아래 문자열 s에 해당 문자가 존재하면
# # # 위치를 출력하고, 존재하지 않으면 "해당 문자가 없습니다."라고 출력하는 프
# # # 로그램을 작성하세요.
# # s2 = "What a beautiful day"

# # client_cha = input("문자 입력")
# # exact_cha = s2.find("{client_cha}")

# # # print(f"s2의 index값: {s2_index}")

# # # if client_cha.find("")
# # if exact_cha == -1:
# #     print("해당 문자가 없습니다.")
# # else:
# #     print(f"해당 값의 index 위치: {s2.index("{exact_cha}")}")

# # # 사용자로부터 여러 개의 단어를 입력을 받은 후 ,(쉼표)로 연결된 문자열로 변
# # # 환하는 프로그램을 작성하세요. 예를들어 aaa bb c ddd를 입력하면
# # # aaa,bb,c,ddd 로 출력하세요

# # cha1 = input("첫번째 단어")
# # cha2 = input("두번째 단어")
# # cha3 = input("세번째 단어")

# # last_cha = ["{cha1}, {cha2}, {cha3}"]
# # # last_cha.split(",")

# # fruits = ["사과", "바나나", "오렌지"]
# # # enumerate 사용
# # for index, fruit in enumerate(fruits):
# #     print(f"{index}: {fruit}")


# # # a = “20231225Rainy” 에서 년, 달, 일, 날씨값을 추출해서 year, month, day,
# # # weather 변수에 입력하고 출력하세요

# # a = "20231225Rainy"
# # # my_list = list(a)

# # year = a[:4]
# # month =  a[4:6]
# # day = a[6:-5]
# # weather = a[-5:]

# # print(f"{year}년 {month}월 {day}일 {weather}")


# # # 문자열 내부의 문자는 아래와 같이 바꿀 수 없다. 아래에서 어떤 방법으로든
# # # 변수를 한 번 이상 이용해서 출력으로 Python이 나오게 하시요.
# # b = "Pithon"

# # result = b.replace("i", "y")
# # print(result)
# # result = b[0] + "y" + b[2:]
# # print(result)


# # • "881120-1068234’ 란 주민번호에서 성별을 나타내는 숫자를 출력하세요
# # • a = “a:b:c:d”를 “a#b#c#d 으로 바꿔서 출력하세요
# # • 5 + 8 = 13 을 .format() 메서드를 이용해서 출력하세요.
# # “현재 시간은 00시 00분 입니다.”.format(), f-string 을 이용해서 출력하세요

# id = "881120-1068234"
# sex = id[7]
# print(f"성별을 나타내는 값: {sex}")

# a = "a:b:c:d"
# result = a.replace(":", "#")
# print(result)

# b = "{} + {} = 13".format(5, 8)
# print(b)

# c = "현재 시간은 00시 00분 입니다."
# first = "현재 시간은 {hour}시 {min}분 입니다.".format(hour=5, min=8)
# print(first)

# hour = 5
# min = 8

# second = print(f"현재 시간은 {hour}시 {min}분 입니다.")

# j = 2
# a = []
# while (j < 5, i > 0):
#     for i in range(9):
#         a.append(j * i)
#         if not i % 9:
#             print(a)
#         else:
#             j += 1

# while j < 5: 
#     i = 1
#     while i <= 9:
#         print(f"{j} X {i} = { j * i }")
#         i += 1
#     print()    
#     j += 1

# sum = 0
# i = 1

# while i <= 10:
#     sum = sum + i
#     i += 1
# print("총합은", sum)


# i = 1
# sum = 0

# while i <= 200:
#     i += 1
#     # print("i", i)
#     if i % 3 != 0:
#         sum += i
# print("3의 배수의 총합은: ", sum)       

# a = "abced"
# i = 0

# while i <= 4:
#     # b = a.index
#     print(f"{a[i]}")
#     i += 1

# i = 0
# sum = 0

# while i < 5:
#     inputValue = int(input("숫자를 입력하세요"))
#     sum = sum + inputValue
#     i += 1
# print("유저가 입력한 5개의 숫자들의 합은: ", sum)    


# i = 0
# while i < 3:
#     print("Hello, Python")
#     i += 1

# low_prices = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]
# difference = []

# for i in range(4):
#     difference.append(high_prices[i] - low_prices[i])
#     i += 1
# print(difference) 


# i = 1
# while i <= 100:
#     if i % 8 == 0 and i % 12 != 0:
#         print(i)
#     i += 1

# F(n) = F(n-1) + F(n-2)

# import random

# randomInt = random.randint(1, 100)
# print("randomInt", randomInt)

# clientInt = -1

# while randomInt != clientInt:
#     clientInt = int(input("숫자를 입력하세요"))
#     if randomInt > clientInt:
#         print("UP")
#         # clientInt = int(input("숫자를 입력하세요"))
#         continue
#     elif randomInt == clientInt:
#         print("CORRECT")
#     else:
#         print("DOWN")
#         continue  

# lst = ["dog", "cat", "parrot", "dog"]
# ret = sorted(lst)
# print(ret)

# lst = [1,2,3,4,5,6]

# avg = sum(lst) / len(lst)
# print(avg)

# lst2 = [1,2,2.2,3.3,4,5]
# lst2.remove(2.2)
# lst2.remove(3.3)
# print(lst2)

# Nums = [1,2,3,4,5,6,7,8,9,10]
# even = []
# odd = []

# for num in Nums:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)
# print("짝수: ", even)
# print("홀수: ", odd)

# string = "AAA/BBB/CCC"

# stringList = string.split("/")
# print(stringList)

# icecream = {"A": 1200, "B": 1200, "C": 1800, "D": 1500, "E": 1000}
# ABC = icecream.values()

# print(sum(ABC))

# i = 0
# while i <= 4: 
#     subject = ["국어", "영어", "수학", "과학", "국사"]
    

# def add_to_num(num1, num2):
#     print(num1 + num2)

# add_to_num(3, 5)

# def calculate_sum(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# print(calculate_sum(1, 2, 3, 4, 5))

# def reverse_string():
#     input_arg = input("문자열을 입력하세요.: ")
#     value = input_arg[::-1]
#     return print(value)

# reverse_string()

# def even_list():
#     input_list = list(input("숫자들을 입력하세요"))
#     int_list = [int(i) for i in input_list]
#     index_input_list = int_list.len() - 1
#     print("index_input_list", index_input_list)
    
#     while i < index_input_list:
#         if int_list[i] % 2 == 0:
#             even_list.append(int_list[i])
#         i += 1
#         else:
#             continue
#     print("even_list", even_list)

    

# even_list()    

# def print_even(lst):
#     for num in lst:
#         if not num % 2:
#             print(num, end="")
# aa = [1,2,3,4,5,6,7,9,2,2,3]

# print_even(aa)

# i = 0
# def make_list(args: str):
#     string_list = list(args)
#     # string_list_index = string_list.len() - 1
#     # while i <= string_list_index:
#     #     # string_list.append(ty)
#     return print(string_list)

# make_list("asdasdasd")

# 호출할 때 마다 인수의 개수가 달라지고, 그 인수 중 가장 큰 수를 구하는
# 함수를 정의하세요. max_args( 20, 14, 72, 58, 10) => 72

# def find_max_num(*args):
#     # if not args:
#     #     return None
#     max_num = args[0]

#     for num in args:
#         # max_num = args[0]
#         if num > max_num:
#             max_num = num
#     return  max_num      

# print(find_max_num(-3,-1,-51,-123))

# def my_fun():
#     return 10, 20

# def my_fun():
#     return (10, 20)


# 두 수를 입력 받아서 함수의 인자로 전달하고 덧셈과 곱셈의 값을 모두 return 하도
# 록 하는 함수를 정의하시고, 덧셈과 곱셈의 값을 받아서 출력하세요.

# def function(arg1: int, arg2: int):
#     add = arg1 + arg2
#     mult = arg1 * arg2

#     # print("add", add)
#     # print("mult", mult)
    
#     value = print(f"두 수의 덧셈: , {add}, 두 수의 곱셈: , {mult}")
#     return value

# function(5,9)


# • 주어진 숫자의 팩토리얼 수를 리턴하는 함수를 정의하세요.

# def factorial(arg: int):
#     i = arg
#     value = 1
#     for i in range(arg, 0, -1):
#           value *= i

#     return value

# print(factorial(5))

# • 공백이 포함된 문자열을 인수로 넣어서 공백으로 분리된 문자열을 키로하고 문자열
# 의 길이를 value로 하는 딕션어리를 만드는 함수를 정의하세요
# make_dict(“I love you”) {‘I’:1, ‘love’:4, ‘you’:3}

# def define_dict(arg: str):
#     my_dict = {}
#     value = arg.split(" ")
#     for s in value:
#         my_dict[s] = len(s)
#     return my_dict

# print(define_dict("아이스아메리카노 카페라떼 콜드브루"))

# • 호출할 때 문자열의 갯수가 달라지도록 복수의 문자열을 입력받아서 각 문자열의
# 길이로 이루어진 리스트를 반환하는 함수를 정의하세요.

# def return_list(*args):
#     the_list = []

#     for word in args:
#         the_list.append(len(word))
        
        
#     return the_list
        
# print(return_list("crazy", "little", "thing"))        

# make_list(‘craze’, ‘little’, ‘thing’, ‘call’, ‘love’) [5, 6, 5, 4, 4]

# • 공백이 포함된 문자열을 입력받아 모든 단어의 첫 글자를 대문자로 변환하는 함수
# 를 정의하세요.
# ‘aBc Def gAb’ -> ‘ABc Def GAb’

# def translate_upper(arg: str):
#     string_list = list(arg)
#     words = arg.split()
#     # print(words)
#     ans = ""

#     for word in words:
#         temp = word[0].upper() + word[1:]
#         ans = ans + " " + temp
#         print("ans:", ans)

#     return ans.strip()

# translate_upper("aBC DeF gAB")    

# def translate_upper2(arg: str):
#     words = arg.split()
#     lst = []
#     for word in words:
#         temp = word[0].upper() + word[1:]
#         lst.append(temp)

#     return "".join(lst)

# translate_upper2("abC DeF gAB")


