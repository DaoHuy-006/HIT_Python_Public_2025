def tinh(luong):
    if luong >= 15000000:
        thue = luong * 0.30
    elif luong >= 7000000:
        thue = luong * 0.20
    else:
        thue = luong * 0.10
    luong_rong = luong - thue 
    return int (thue), int (luong_rong)
luong = int(input("\nInput: "))
thue, luong_rong = tinh(luong)
print(f"Output: Thuế: {thue} Thu nhập: {luong_rong}\n")
print("\n")