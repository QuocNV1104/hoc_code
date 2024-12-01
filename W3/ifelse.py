# Cau lenh dieu kien

""" Vi du 1: tinh tong cua 2 so bat kì, in ra so do, neu tong 2 so lon hon 10, nguoc lai in ra thong bao so qua nho"""

a = 6
b = 3

tong = a + b

# if(tong > 10):
#     print("tong hai so:", tong)
# else:
#     print("hai so qua nho!")

"""
Vi du 1: Tinh tong 2 so bat kì, in ra so do, neu tong hai so lon hon 10, nguoc lai, in ra hieu cua hai so neu tong cua chung nho hon hoac bang 10 va lon hon 0
nguoc lai, in ra thong bao so qua nho!
"""
if(tong > 10):
    print("tong hai so:", tong)
elif(tong <= 10 and tong > 0):
    print("hieu cua hai so:", a-b)
else:
    print("hai so qua nho")