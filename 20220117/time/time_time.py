from calendar import MONDAY
from ctypes.wintypes import HACCEL
from platform import java_ver
from socket import J1939_PGN_ADDRESS_COMMANDED
import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())
print(time.strftime('출력할 형식 포맷 코드', time.localtime(time.time())))

# %a 요일 줄임말 Mon
# %A 요일 MONDAY
# %b 달 줄임말 Jan
# %B 달 January
# %c 날짜와 시간을 출력 06/01/01/17:22:21
# %d 날(day) [01,31]
# %H 시간(hour)-24시간 출력 형태 [00,23]
# %l 시간(hour)-12시간 출력 형태 [01,12]
# %j 1년 중 누적 날짜 [001,366]
# %m 달 [01,12]
# %M 분 [01,59]
# %p AM or PM AM
# %S 초 [00,59]
# %U 1년 중 누적 주-일요일을 시작으로 [00,53]
# %w 숫자로 된 요일 [0(일요일),6]
# %W 1년 중 누적 주-월요일을 시작으로 [00,53]
# %x 현재 설정된 로케일에 기반한 날짜 출력 22/01/18
# %X 현재 설정된 로케일에 기반한 시간 출력 17:22:21
# %Y 년도 출력 2022
# %Z 시간대 출력 대한민국 표준시
# %% 문자 %
# %y 세기부분을 제외한 년도 출력 22