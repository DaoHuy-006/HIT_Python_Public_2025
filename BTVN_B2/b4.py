tien = int(input("\nInput: "))
mua_bia = tien //28
vo_bia = mua_bia
tong_bia = mua_bia
while vo_bia >= 3:
    tang_bia = vo_bia // 3
    tong_bia += tang_bia
    vo_bia = vo_bia % 3 + tang_bia
print("Output: Số chai bia có thể mua được là: ",tong_bia)

