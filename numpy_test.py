import numpy as np

arr1d = np.array([1,2,3,4,5])
arr2d = np.array([[1,2,3],[4,5,6]])
print("1차원 배열\n", arr1d)
print("2차원 배열", arr2d)

print("1차원 배열 형태:", arr1d.shape)
print("2차원 배열 형태:", arr2d.shape)
print("1차원 배열 데이터 타입:", arr1d.dtype)

print("1차원 배열 첫번째 요소:", arr1d[0])
print("2차원 배열 (1,2) 요소:", arr2d[1,2])
print("2차원 배열 첫 줄:", arr2d[0,:])

arr2d_reshaped = arr2d.reshape(1, 6)
print(arr2d_reshaped)
# arr2d_reshaped2 = arr2d.reshape(1, 2, 3)
# print(arr2d_reshaped2)

a = np.array([1,5,8,10])
cond = a > 5
print(cond)
# print(cond) => [False False True True]
# print(a[a > 5]) => #[8 10]

# a = np.array([[1,5,8,10], [9,3,7,2]])
# print(a)
# cond = a > 5

b = np.zeros(10)
print(b)

c = np.ones((2,3))
print(c)

result = np.arange(1, 11)
print(result)

a = np.array([[1,2,3], [4,5,6]]) #  a의 배열에 대한 형태와 차원수
print("배열 a의 형태 (Shape):", a.shape)
print("배열 a의 차원수 (ndim):", a.ndim)  
print("배열 a의 원소 개수 (Size):", a.size)

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(a[1:,1:])

a = np.array([[1,2], [3,4], [5,6]])
b = a.reshape(6)
print(b)
c = a.flatten()
print(c)

a = np.array([1,5,6,8,2,10])
cond = a > 5

print(cond)
print(a[cond])

a = np.array([[[[1,2,3,4]]]]).shape
print(a)