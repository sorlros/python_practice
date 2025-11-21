import pandas as pd

# # # df = pd.DataFrame({
# # #     'age': ['23', '45', '30'],
# # #     'name': ['Tom', 'Jane', 'Alex']
# # # })

# # # print(df)

# # # print(df.dtypes)
# # # age = df["age"].astype(int)
# # # print(age)


# # d = {'Num':[1,2,3,4,5], 'City':['Pusan', 'Seoul', 'Ulsan', 'Suwon', 'Sejong']}
# # d = {'City':['Pusan', 'Seoul', 'Ulsan', 'Suwon', 'Sejong']}
# # df = pd.DataFrame(d)
# # print(df)
# #print(df.index)
# # df = df.set_index('Num')

# # # index reset  # inplace = 원본 값을 변경하거나(True)
# # # df.reset_index(inplace=True) 

# # #  변경하지 않고 값으로 지정하고싶을 때(False)
# # # df2 =df.reset_index(inplace=True)

# # # df.set_index("Num", inplace=True)

# df['Population'] = [300, 1000, 100, 150, 50]
# df['Job'] = [100, 900, 300, 400, 200]
# # # print(df)
# # print("---------------------------")

# # # 2개의 column 내용을 출력
# # # print(df[["City", "Job"]])
# # print("---------------------------")

# # # 특정 행을 선택
# # # print(df.loc[1])
# # print("---------------------------")

# # # 복수 행을 선택
# # # print(df.loc[[1,3]])
# # print("---------------------------")

# # # 행을 생성
# # # df.loc[10] = [8,"Daegoo",500,300]
# # # print(df)
# # print("---------------------------")

# # # df.shape() # (7,3)

# # # 컬럼별 평균, 합 구하기
# # # print(df["Job"].mean(), 2) # 반올림 후 소숫점 2자리까지
# # # df["Job"].sum()

# # # 컬럼명만 출력
# # # df.columns

# # # 특정 셀 데이터 
# # # print(df.loc[3, "City"])

# # # 복수개의 셀 데이턴
# # # print(df.loc[[1, 3], ["City", "Job"]])

# # # Boolean Indexing
# # # print(df["Population"] > 100) # True False로 출력

# # # 조건에 만족하는 모든 데이터만 출력
# # # cond = df["Population"] > 100
# # # print(df[cond]) 

# # # 조건에 충족하는 특정 열 데이터
# # # df["Population"] > 100[["City", "Job"]] 
# # # df.loc[df["Population"] > 100, ["City", "Job"]]


# # # loc 를 이용한 slicing 에서는 마지막 주소 데이터를 포함한다
# # # print(df.loc[1:"Six"])
# # # print(df.loc[1:3])

# # df.reset_index()
# # df.set_index("City", inplace=True)
# # print(df)

# # # print(df["Seoul":"Suwon"])

# # # iloc를 이용한 슬라이싱
# # # print(df.iloc[1])
# # # print("---------------------")
# # # print(df.iloc[[1,3]])
# # print("---------------------")
# # print(df)
# # # print(df.iloc[[0,2], [0,1]])
# # print("---------------------")
# # print(df.iloc[:2, :2])

# # print(df)
# # # 행 삭제
# # # df.drop(index=5, inplace=True)

# # # 특정 열 삭제
# # # df.drop("Job", axis=1, inplace=True)
# # b = df.drop("Job", axis=1) # axis=0 (기본값 상태이며 행단위 제거) axis=1 열단위 제거
# # print(b)
# # # print(df)

# # # Dataframe 합치기
# # dfa = pd.DataFrame([[1,2],[3,4]])

# # # axis= 0 행 방향으로 추가
# # dfb = pd.DataFrame([[5,6]])
# # result1 = pd.concat([dfa, dfb], axis=0, ignore_index=True)
# # print("axios=0 \n", result1)

# # print("-"*100)

# # # axis=1 열방향으로 추가
# # dfc = pd.DataFrame([[5],[6]])
# # result2 = pd.concat([dfa, dfc], axis=1, ignore_index=True)
# # print("axios=1 \n", result2)

# # #--------------------------------------------------------------------------------------
# d = {'Num':[1,2,3,4,5,6], 'City':['Pusan', 'Seoul', 'Ulsan', 'Suwon', 'Sejong', 'Daegoo']}
# df = pd.DataFrame(d).set_index('Num')
# df['color'] = ['green', 'blue', 'red', 'green', 'red', 'green']
# df['Jobs'] = [100, 900, 300, 400, 200, 85]
# print(df)

# # groupby 그룹화 groupby(‘컬럼명’)


# # count(): 각 value 개수
# print(df["Jobs"].count())

# # sum(): 각 value 합
# print(df["Jobs"].sum())

# # max(): 해당 value 최대 값
# print(df["Jobs"].max())


# # #--------------------------------------------------------------------------------------
# d = {'Flower':['Rose','Sunflower','Tulip','Cherry Blossom','Daisy','Hibiscus'], 'City':['Pusan', 'Seoul', 'Ulsan', 'Suwon', 'Sejong', 'Jeju']}
# df3 = pd.DataFrame(d)

# # merge()
# # "City"를 기준으로 merge  inner: 양쪽 모두 존재하는 값들만
# inner_merge = pd.merge(df, df3, on="City", how="inner") 
# print(inner_merge) # df에만 존재하는 "Jeju" 삭제됨
# print("-------------------------------------------------------")

# # how="left": 왼쪽 Dataframe 값은 모두 출력
# left_merge = pd.merge(df, df3, on="City", how="left")
# print(left_merge)
# print("-------------------------------------------------------")

# # how="right": 오른쪽 Dataframe 값은 모두 출력
# right_merge = pd.merge(df, df3, on="City", how="right")
# print(right_merge)
# print("-------------------------------------------------------")



# DataFrame 에서 결측치 처리
# 결측치(Missing Value) 
# - 데이터가 비어있거나(None, NaN) 기록되지 않은 값
# - 분석/모델링 시 오류 또는 왜곡을 일으킴
# - pandas에서는 결측치를 NaN으로 표현

# fillna(0) 
# - 모든 NaN을 0으로 변경
# - 열 별로 다른 값을 채울수 있음
# df.fillna({
#   "A": 0,
#   "B": df["B"].mean()
# })

df = pd.DataFrame({
    'name': ['Kim', 'Lee', None, 'Park'],
    'age': [25, None, 30, 35],
    'score': [90, 85, None, None]
})
print(df)
print("-------------------------------------------------------")
# 컬럼 별로 결측치 확인
print(df.isnull().sum())
print("-------------------------------------------------------")
print(df.isna().sum())
print("-------------------------------------------------------")

# 결측치 열 삭제
df_drop = df.dropna()
print(df_drop)
print("-------------------------------------------------------")

# 결측치 0 으로 채우기
df_fill = df.fillna(0)
print(df_fill)
print("-------------------------------------------------------")


# 예제

df_practice = pd.DataFrame({
"name": ["Kim", "Lee", "Park"],
"age": [24, 30, 21],
"score": [88, 92, 79]
})

print(df_practice)
print("-------------------------------------------------------")

print(df_practice["name"])
print("-------------------------------------------------------")

cond = df_practice["score"] >= 80
df_practice["passed"] = cond
print(df_practice)
print("-------------------------------------------------------")

cond2 = df_practice["age"] > 25
# df_practice[] > cond2
# print(df_practice)
print("age > 25 인 모든값 출력", df_practice[cond2])


print("df에서 age가 25이상이며 score 값이 90이상인 데이터의 DataFrame 모든 값을 출력하세요")
cond3 = (df_practice["age"] >= 25) & (df_practice["score"] >= 90)
print(df_practice[cond3])
print("-------------------------------------------------------")

print("age와 score 값의 평균값을 각각 출력하세요.")
print("age의 평균값: ", df_practice["age"].mean())
print("score의 평균값: ", df_practice["score"].mean(), 2)
print("-------------------------------------------------------")

df2 = pd.DataFrame({
"dept": ["HR", "HR", "IT", "IT", "Sales"],
"salary": [4000, 4200, 5000, None, 4500]
})

print("결측치를 평균으로 채우세요")

# df2.fillna(0)
# print(df2["salary"].mean())
value = df2["salary"].mean()  # 평균값
df2["salary"].fillna(value)
# print("AAAAAAA")
# df2["salary"][3] = value
print(df2)

# print(df2.isna().mean())

rs = df2.groupby("dept")
print(rs["salary"].mean())