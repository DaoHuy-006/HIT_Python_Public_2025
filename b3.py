n = int(input("\nInput: "))
def dem_va_tinh_tong(n):
    so_chu_so = 0
    tong = 0
    so = n
    while n > 0:
         chu_so = n % 10
         tong += chu_so
         so_chu_so += 1
         n = n // 10
    return so, so_chu_so, tong
so, so_chu_so, tong = dem_va_tinh_tong(n)
print(f"Output: Số chữ số: ",so_chu_so, "Tổng chữ số: ",tong)

 