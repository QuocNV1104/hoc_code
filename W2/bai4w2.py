n = int(input("n="))
A = []
B = []
for i in range(0, n):
    x = int(input("Nhập x:"))
    A.append(x)
for i in range (0, n):
    y = int(input("Nhập y:"))
    B.append(y)
print("Các cặp phần tử A và B:")
for i in range(n):
    print(f"{A[i]}: {B[i]}")