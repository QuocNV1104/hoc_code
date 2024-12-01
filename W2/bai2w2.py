E = [2,3,4.5, "hello", 6,7]

count_i = 0
count_f = 0
count_s = 0

for item in E:
    if isinstance (item, int):
        count_i += 1
    elif isinstance (item, float):
        count_f += 1
    elif isinstance(item,str):
        count_s += 1
print("Các số nguyên:", count_i)
print("Các số thực:", count_f)
print("Chuỗi ký tự:", count_s)
    
n = int(input("Nhập số nguyên dương n:"))

A = [i for i in range(1, n+1) if n %i==0]
B = [i for i in range(1,n) if n % i!=0]
print("Tập A:", A)
print("Tập B:", B)