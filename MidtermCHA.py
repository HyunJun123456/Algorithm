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

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#