# Nhập hai chuỗi từ bàn phím
s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhập chuỗi s2: ")

# In ra đảo ngược của s1
print("Đảo ngược s1:", s1[::-1])

# Nhập a, b và kiểm tra điều kiện
a = int(input("Nhập a (vị trí bắt đầu): "))
b = int(input("Nhập b (vị trí kết thúc): "))

if 1 <= a < b <= len(s2):
    # Cắt và đảo ngược đoạn từ vị trí a đến b (chỉ số Python từ 0)
    # Trừ 1 vì Python đánh chỉ số từ 0
    s2_reversed = s2[:a-1] + s2[a-1:b][::-1] + s2[b:]
    print("s2 sau khi đảo ngược đoạn từ a đến b:", s2_reversed)
else:
    print("Giá trị a, b không hợp lệ.")

# Tạo s3: xóa ký tự ở vị trí chẵn trong s1 (index 0, 2, 4...)
s3 = ""
for i in range(len(s1)):
    if i % 2 != 0:     # chỉ lấy vị trí lẻ
        s3 += s1[i]
print("s3 (s1 sau khi xóa ký tự ở vị trí chẵn):", s3)
# Tạo s4: đan xen chuỗi s1 và s2
min_len = min(len(s1), len(s2))
s4 = ""
for i in range(min_len):
    s4 += s1[i] + s2[i]
s4 += s1[min_len:] + s2[min_len:]
print("s4 (đan xen s1 và s2):", s4)