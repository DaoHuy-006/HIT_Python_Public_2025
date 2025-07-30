# Nhập vào họ tên từ bàn phím
name = input("Nhập họ tên: ")
# Xóa khoảng trắng dư thừa ở đầu/cuối, chia chuỗi thành các từ.
words = name.strip().split()
# Viết hoa chữ cái đầu mỗi từ, còn lại viết thường.
normalized_words = [word.capitalize() for word in words]
# Ghép lại thành chuỗi hoàn chỉnh.
normalized_name = ""
for word in normalized_words:
    normalized_name += word + " "
normalized_name = normalized_name.strip()
# In kết quả
print("Họ tên sau chuẩn hóa:", normalized_name)