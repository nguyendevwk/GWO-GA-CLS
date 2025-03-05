# Description: Chuyển đổi dữ liệu từ dạng dọc sang dạng ngang và ghi vào file CSV tổng hợp
import pandas as pd

file_name = 'comparison_function'  # Chỉnh sửa tên file CSV
dim = 10  # Chỉnh sửa kích thước của hàm thử nghiệm (dim10, dim30, dim50, dim100)

# Đọc dữ liệu từ file CSV
f1_data = pd.read_csv(f"./dim{dim}/{file_name}_F1_{dim}.csv")
f2_data = pd.read_csv(f"./dim{dim}/{file_name}_F2_{dim}.csv")
f3_data = pd.read_csv(f"./dim{dim}/{file_name}_F3_{dim}.csv")
f4_data = pd.read_csv(f"./dim{dim}/{file_name}_F4_{dim}.csv")
f5_data = pd.read_csv(f"./dim{dim}/{file_name}_F5_{dim}.csv")
f6_data = pd.read_csv(f"./dim{dim}/{file_name}_F6_{dim}.csv")
f7_data = pd.read_csv(f"./dim{dim}/{file_name}_F7_{dim}.csv")
f8_data = pd.read_csv(f"./dim{dim}/{file_name}_F8_{dim}.csv")
f9_data = pd.read_csv(f"./dim{dim}/{file_name}_F9_{dim}.csv")


# Chuyển đổi dữ liệu sang dạng ngang
f1_pivot = f1_data.T
f2_pivot = f2_data.T
f3_pivot = f3_data.T
f4_pivot = f4_data.T
f5_pivot = f5_data.T
f6_pivot = f6_data.T
f7_pivot = f7_data.T
f8_pivot = f8_data.T
f9_pivot = f9_data.T


# Đổi tên cột đầu tiên thành tên các hàm
f1_pivot.columns = f1_pivot.iloc[0]
f2_pivot.columns = f2_pivot.iloc[0]
f3_pivot.columns = f3_pivot.iloc[0]
f4_pivot.columns = f4_pivot.iloc[0]
f5_pivot.columns = f5_pivot.iloc[0]
f6_pivot.columns = f6_pivot.iloc[0]
f7_pivot.columns = f7_pivot.iloc[0]
f8_pivot.columns = f8_pivot.iloc[0]
f9_pivot.columns = f9_pivot.iloc[0]


# Bỏ hàng đầu tiên sau khi đổi tên cột
f1_pivot = f1_pivot[1:]
f2_pivot = f2_pivot[1:]
f3_pivot = f3_pivot[1:]
f4_pivot = f4_pivot[1:]
f5_pivot = f5_pivot[1:]
f6_pivot = f6_pivot[1:]
f7_pivot = f7_pivot[1:]
f8_pivot = f8_pivot[1:]
f9_pivot = f9_pivot[1:]


# Tạo file CSV tổng hợp
with open('combined_functions_10.csv', 'w') as f:
    f.write("Function Test F1\n")
    f1_pivot.to_csv(f, header=True)
    f.write("\nFunction Test F2\n")
    f2_pivot.to_csv(f, header=True)
    f.write("\nFunction Test F3\n")
    f3_pivot.to_csv(f, header=True)
    f.write("\nFunction Test F4\n")
    f4_pivot.to_csv(f, header=True)
    f.write("\nFunction Test F5\n")
    f5_pivot.to_csv(f, header=True)
    f.write("\nFunction Test F6\n")
    f6_pivot.to_csv(f, header=True)
    f.write("\nFunction Test F7\n")
    f7_pivot.to_csv(f, header=True)
    f.write("\nFunction Test F8\n")
    f8_pivot.to_csv(f, header=True)
    f.write("\nFunction Test F9\n")
    f9_pivot.to_csv(f, header=True)

print("Dữ liệu đã được ghi vào file 'combined_functions_10.csv'")
