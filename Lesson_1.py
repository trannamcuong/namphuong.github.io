

#Homework_1: Tinh dien tich hinh tron
radius=float(input('Nhap_ban_kinh_duong_tron:'))
Area=3.14*radius**2
print('Dien tich duong tron=', Area)

#Homework_2: Tinh gia tri F
x=float(input('Nhap gia tri cho x:'))
y=float(input('Nhap gia tri cho y:'))
z=float(input('Nhap gia tri cho z:'))
import math
F=(x+y+z)/(x**2+y**2+1)-abs(x-z*math.cos(y))
print('Gia tri cua F=', F)

"""
#Homework_3: 7 bien khong hop le
7bien
@homework
Homework 3
17-December
Math
import
pi

#Homework_4: 7 bien hop le
Bien1
Bien_2
_Bien3
BIEN4
ABCDEF12345
abcdef_12345
va_ri_able_7
"""

"""
Homework_5: Tìm hiểu về module math trong Python rồi trả lời các câu hỏi sau:
1. Module đó có mục đích gì?: được định nghĩa là các hàm toán học phổ biến nhất,bao gồm các hàm lượng giác, hàm số, hàm logarit, v.v. 
Ngoài ra, nó cũng định nghĩa hai hằng số toán học, tức là số Pie và Euler
2. Kể tên một số thứ trong nó hay dùng hoặc bạn thấy ấn tượng? 
- pi, e, 
- cos, sin, log, log10, exp 
- sqrt, abs
"""
import math
print('pi=', math.pi)
print('|abs(-5)|=', math.abs(-5))

