n = int(input("Nhap vao so nguyen n:"))
if(n%400==0):
    print("Day la nam nhuan")
elif(n%4 ==0 and n%100 != 0):
    print("Day la nam nhuan")
else:
    print("Khong phai nam nhuan")