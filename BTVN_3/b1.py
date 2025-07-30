
n = int(input("Nhập số lượng phần tử n: "))
list = []
for i in range(n):
    num = int (input(f"Nhập phần tử thứ {i+1}: "))
    list.append(num)
print("List ban đầu: ",list)

x = int(input("Nhập số x cần kiểm tra: "))
count_x = list.count(x)
print(f"Số {x} xuất hiện {count_x} lần trong list")

if len(list) >= 7:
    list[1:7] = [8, 5, 4, 0, 1, 3]
else:
    print("List không đủ dài để thay thế từ vị trí 2 đến 7")
print("List sau khi thay thế: ",list)

max_val = max(list)
min_val = min(list)
print(f'Số lớn nhất: {max_val}')
print(f'Số nhỏ nhất: {min_val}')

y = int(input("Nhập số y để chèn vào đầu list: "))
list.insert(0,y)
print("List sau khi chèn y vào đầu: ",list)

if list == sorted(list):
    print("Tăng")
elif list == sorted(list, reverse=True):
    print("Giảm")
else:
    print("No")