# 색과 값에 대한 저항 생성
resistor = {"black":0, "brown":1, "red":2, "orange":3, "yellow":4, "green":5, "blue":6, "violet":7, "grey":8, "white":9}

color1 = input()
color2 = input()
color3 = input()

# 발견한 규칙을 적용. - (a*10+b) * 10^c
result = (resistor[color1]*10 + resistor[color2]) * (10 ** resistor[color3])
print(result)