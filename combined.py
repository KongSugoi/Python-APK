import pandas as pd
import os

# Đường dẫn tới thư mục chứa các file CSV
folder_path = 'D:\BTL_PYTHON\CNN'

# Danh sách để chứa dữ liệu từ mỗi file
rows_list = []

# Lặp qua mỗi file csv trong thư mục
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    if file.endswith('.csv') and os.path.isfile(file_path):
        # Đọc dữ liệu từ file CSV
        df = pd.read_csv(file_path)
        
        # Chuyển đổi dữ liệu thành dictionary với keys là Function và values là Vector_0
        data_dict = dict(zip(df['Function'], df['Vector_0']))
        
        # Thêm dictionary vào list rows_list
        rows_list.append(data_dict)

# Đặt index cho mỗi hàng theo tên file CSV
index_list = [os.path.splitext(file)[0] for file in os.listdir(folder_path) if file.endswith('.csv')]

# Tạo DataFrame từ rows_list với index là index_list
result_df = pd.DataFrame(rows_list, index=index_list)

# Điền 0 vào những ô còn trống
result_df = result_df.fillna(0)

# Xuất kết quả ra file CSV mới
output_file_path = 'convert_done.csv'
result_df.to_csv(output_file_path)

print(f"Đã gộp dữ liệu thành công. Vui lòng kiểm tra file '{output_file_path}'")
