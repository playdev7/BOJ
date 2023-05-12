# https://solved.ac/profile/playdev7
# 1340 - 연도진행바
# 문제 요약 - 현재 날짜가 분까지 주어지면 그 해의 전체 시간 중 몇 퍼센트가 지났는지 출력하는 프로그램 작성.

# 윤년일 때는 2월이 29일이다.
# 윤년은 그 해가 400으로 나뉘어 떨어지거나 4로 나뉘어지면서 100으로 나누어 떨어지지 않는 해 일 때 이다.

# 평년 클래스 생성
class Year:
    # 필요한 초기 필드 선언
    # 평년의 날짜 리스트
    day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 해당 연도의 모든 시간
    all_minute = 0
    # 1월 1일부터 현재까지의 모든 시간
    current_minute = 0


    # 해당 연도의 모든 시간을 분으로 구하는 메소드 선언.
    def get_all_minute(self):
        for i in self.day_list:
            self.all_minute += i
        # 하루는 1440 분
        self.all_minute *= 1440
        return self.all_minute
    

    # 1월 1일부터 현재 까지의 모든 날을 구하는 메소드 선언
    def get_current_minute(self, month, day, hour, minute):
        # month-1번 인덱스까지 대입하면 직전 달 까지의 모든 날이 구해짐
        for i in range(month-1):
            self.current_minute += self.day_list[i]
        # 이후에 day까지 더해주면 오늘까지의 모든 날이 됨.
        self.current_minute += day
        
        # 하루를 빼서 어제로 만들고 1440을 곱해서 오늘까지의 모든 분을 구함
        self.current_minute -= 1
        self.current_minute *= 1440

        # 이후 hour * 60 (분)을 더해줌
        self.current_minute += hour * 60
        # 이후 현재의 분을 더해줌
        self.current_minute += minute

        return self.current_minute
    
    # 올해의 모든 시간이 100이면, 현재 시간이 몇 퍼센트인지를 반환하는 메소드 선언
    def percentage(self):
        # 해당 연도의 모든분 / 현재까지의 모든 분 * 100 %
        return self.current_minute / self.all_minute * 100
    

# 평년 클래스를 상속받은 윤년 클래스 생성
class Leap_year(Year):
    # day_list만 29로 수정.
    def __init__(self):
        self.day_list[1] = 29

# 문자열 month를 숫자로 변형시켜주는 month4int 함수 선언
def month4int(str):
    month_dict = {
        "January" : 1,
        "February" : 2,
        "March" : 3,
        "April" : 4,
        "May" : 5,
        "June" : 6,
        "July" : 7,
        "August" : 8,
        "September" : 9,
        "October": 10,
        "November" : 11,
        "December": 12,
    }

    return month_dict[str]


# 메인함수
def main():
    # 일단 입력 받아서 month, day, year, hour, minute 으로 나눔.
    date = input().split(", ")
    month, day = date[0].split()
    year, time = date[1].split()
    hour, minute = time.split(":")
    
    # 모든 정보를 정수로 변환
    year = int(year)
    month = month4int(month)
    day = int(day)
    hour = int(hour)
    minute = int(minute)

    # 윤년은 그 해가 400으로 나뉘어 떨어지거나 4로 나뉘어지면서 100으로 나누어 떨어지지 않는 해 일 때 이다.
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        # 윤년 객체 생성 후 메소드 적용
        Leap = Leap_year()
        Leap.get_all_minute()
        Leap.get_current_minute(month, day, hour, minute)
        print(Leap.percentage())
    
    # 평년일 경우 Year 객체 생성 후 메소드 적용.
    else:
        Plain = Year()
        Plain.get_all_minute()
        Plain.get_current_minute(month, day, hour, minute)
        print(Plain.percentage())

if __name__ == "__main__":
    main()