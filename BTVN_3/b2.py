k = int (input("Nhập số phần tử của list a: "))

a = []
print("Nhập các phần tử của list:")
for i in range(k):
    val = int(input(f"Phần tử thứ {i+1}: "))
    a.append(val)

n = int(input("Nhập số dòng n: "))
m = int(input("Nhập số cột m: "))

if n * m > k:
    print("No")
else:
    x = []
    index = 0
    for i in range(n):
        row = []
        for j in range(m):
            row.append(a[index])
            index += 1
        x.append(row)

print("Ma trận x: ")
print(x)
