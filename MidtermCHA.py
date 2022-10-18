# 021 문자열 인덱싱(1)
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letter = 'python'
print(letter[0], letter[2])

# 025 문자열 치환(2)
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)

# 029 replace 메서드(3)
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)

# 033 문자열 곱하기(4)
# 화면에 '-'를 80개 출력하세요.
print("-"*80)

# 035 문자열 출력(5)
# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
name1 ="김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

# 038 컴마 제거하기(6)
# 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
stock = "5,969,782,550"
stockNoComma = stock.replace(",", "")
intStockNoComma = int(stockNoComma)
print(intStockNoComma, type(intStockNoComma))


# 040 strip 메서드(7)
# 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
data = "        삼성전자     "
dataTrim = data.strip()
print(dataTrim)

# 042 lower 메서드(8)
# 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
ticker = "BTC_KRW"
ticker = ticker.lower()
print(ticker)

# 045 endswith 메서드(9)
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
file_name = "보고서.xlsx"
file_name.endswith(("xlsx", "xls"))
if(file_name.endswith(("xlsx", "xls"))):
    print("파일 이름이 xlsx 또는 xls이 맞음")
else: 
    print("파일 이름이 xlsx 또는 xls이 아님")

# 048 split 메서드(10)
# 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
ticker = "btc_krw"
ticker = ticker.split("_")
print(ticker)

# 053(11)
# movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 054(12)
# movie_rank 리스트에서 '럭키'를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]
print(movie_rank)

# 055(13)
# movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

# 057(14)
# 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
nums = [1, 2, 3, 4, 5, 6, 7]
print("max: ", max(nums))
print("min: ", min(nums))

# 058(15)
# 다음 리스트의 합을 출력하라.
nums = [1, 2, 3, 4, 5]
print(sum(nums))

# 061(16)
# price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 062(17)
# 슬라이싱을 사용해서 홀수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 064(18)
# 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
nums = [1, 2, 3, 4, 5]
print(nums[::-1])


# 066 join 메서드(19)
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

# 070 리스트 정렬(20)
# 리스트에 있는 값을 오름차순으로 정렬하세요.
data = [2, 4, 3, 1, 5, 10, 9]
dataSort = sorted(data)
print(dataSort)

# 071(21)
# my_variable 이름의 비어있는 튜플을 만들라.
my_variable = ()
print(my_variable)

# 072(22)
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)

# 073(23)
# 숫자 1 이 저장된 튜플을 생성하라.
my_tuple = (1, )
print(my_tuple)

# 074(24)
# 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
"""
>> t = (1, 2, 3)
>> t[0] = 'a'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    t[0] = 'a'
TypeError: 'tuple' object does not support item assignment
"""
# 튜플은 원소를 변경할 수 없기 때문에

# 075(25)
# 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
t = 1, 2, 3, 4
print(type(t))

# 076(26)
# 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
t = ('a', 'b', 'c')
t = ("A", "b", "c")
print(t)

# 077(27)
# 다음 튜플을 리스트로 변환하라.
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)
print(data)

# 078(28)
# 다음 리스트를 튜플로 변경하라.
interest = ['삼성전자', 'LG전자', 'SK Hynix']
data = tuple(interest)
print(data)

# 079 튜플 언팩킹(29)
# 다음 코드의 실행 결과를 예상하라.
"""
    temp = ('apple', 'banana', 'cake')
    a, b, c = temp
    print(a, b, c)
"""
# 각각의 a, b, c에 값이 저장되어 apple banana cake가 나온다

# 080 range 함수(30)
# 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
data = tuple(range(2,100,2))
print(data)

# 082(31)
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *valid_score = scores
print(valid_score)

# 083(32)
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *valid_score, b = scores
print(valid_score)

# 087(33)
# 다음 딕셔너리를 사용하여 메로나 가격을 출력하라.
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print("메로나 가격:",ice["메로나"])

# 088(34)
# 다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라.
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
ice['메로나'] = 1300
print(ice)

# 090(35)
# 다음 코드에서 에러가 발생한 원인을 설명하라.
"""
>> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
>> icecream['누가바']
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    icecream['누가바']
KeyError: '누가바'
"""
# icecream에서 없는 값을 찾기 때문에 생기는 오류

# 092 딕셔너리 인덱싱(36)
# inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
print(inventory['메로나'][0], '원')

# 095 딕셔너리 keys() 메서드(37)
# 다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
key = list(icecream.keys())
print(key)

# 096 딕셔너리 values() 메서드(38)
# 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
dic = list(icecream.values())
print(dic)

# 098 딕셔너리 update 메서드(39)
# 아래의 new_product 딕셔너리를 다음 icecream 딕셔너리에 추가하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

# 099 zip과 dict(40)
# 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

# 102(41)
# 아래 코드의 출력 결과를 예상하라
print(3 == 5)
# False

# 104(42)
# 아래 코드의 결과를 예상하라.
x = 4
print(1 < x < 5)
# True

# 108(43)
# 아래 코드의 출력 결과를 예상하라
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")
# Hi, there.

# 112(44)
# 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.
"""    
number = input("숫자를 입력하세요: ")
print(10+int(number))
과제 진행을 위해 테스트 후 주석 처리 해두었습니다.
"""

# 116(45)
# 사용자로부터 입력 받은 시간이 정각인지 판별하라.
"""
>> 현재시간:02:00
정각 입니다.
>> 현재시간:03:10
정각이 아닙니다
"""
"""
time = input("현재시간: ")
if (time[-2:] == "00"):
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")
"""

# 118(46)
# 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 
# 투자 경고 종목이라면 '투자 경고 종목입니다'를 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
"""
invest = input("종목명: ")
if invest in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")
"""

# 121(47)
# 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.
"""
letter = input("")
if letter.islower():
    print(letter.upper())
else:
    print(letter.lower())
"""

# 124(48)
# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
"""
>> input number1: 10
>> input number2: 9
>> input number3: 20
"""
"""
num1 = input("input number1: ")
num2 = input("input number2: ")
num3 = input("input number3: ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
if(num1 >= num2 and num1 >= num3):
    print(num1)
elif(num2 >= num1 and num2 >= num3):
    print(num2)
else:
    print(num3)
"""

# 127(49)
# 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다. 
# 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.
"""
rrNo = input("주민등록번호: ")
rrNo = rrNo.split("-")[1]
if rrNo[0] == "1" or rrNo[0] == "3":
    print('남자')
else:
    print('여자')
"""

# 130(50)
# 아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.
import requests

btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
"""
btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다. 
최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 
그렇지 않은 경우 "하락장" 문자열을 출력하라.
"""
move = float(btc['max_price']) - float(btc['min_price'])
first = float(btc['opening_price'])
high = float(btc['max_price'])

if(first+move) > high:
    print("상승장")
else:
    print("하락장")

# 139(51)
# 다음 코드를 for문으로 작성하라.
"""
print("++++")
print(10)
print(20)
print(30)
"""
print("+++")
for x in [10,20,30]:
    print(x)

# 143(52)
# 리스트에 주식 종목이름이 저장돼 있다.
list = ["SK하이닉스", "삼성전자", "LG전자"]
for x in list:
    length = len(x)
    print(length)

# 151(53)
# 리스트에는 네 개의 정수가 저장돼 있다.
list = [3, -20, -3, 44]
for x in list:
    if x <0:
        print(x)

# 158(54)
# 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split() 메서드)
list = ['hello.py', 'ex01.py', 'intro.hwp']
list1 = list[0].split(".")
print(list1[0])
list2 = list[1].split(".")
print(list2[0])
list3 = list[2].split(".")
print(list3[0])


# 160(55)
# 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.
list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for x in list:
    split =x.split(".")
    if(split[1] == "h" or split[1] == "c"):
        print(x) 

# 164(56)
# 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라.
for i in range(100):
    print(99-i)

# 174(57)
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
"""
100 32150
110 32000
120 32500
"""
price_list = [32100, 32150, 32000, 32500]
for i in range(1, 4):
    print(90+10*i, price_list[i])

# 186(58)
# 리스트에 저장된 데이터를 아래와 같이 출력하라.
apart = [ [101, 102], [201, 202], [301, 302] ]
for y in apart[::-1]:
    for x in y:
        print(x, "호")

# 191(59)
# data에는 매수한 종목들의 OHLC (open/high/low/close) 가격 정보가 바인딩 되어있다.
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
# 수수료를 0.014 %로 가정할 때, 각 가격에 수수료를 포함한 가격을 한라인에 하나씩 출력하라.
for x in data:
    for y in x:
        print(y * 1.00014)

# 196(60)
# ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 종가가 150원보다 큰경우에만 종가를 출력하라.
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for x in ohlc[1:]:
    if (x[3] > 150):
        print(x[3])

