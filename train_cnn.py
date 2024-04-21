import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Đọc dữ liệu từ file CSV
data = pd.read_csv("vectors.csv")

# Chia dữ liệu thành dữ liệu đầu vào và nhãn (nếu có)
X = data.drop(columns=["Function"])  # Loại bỏ cột nhãn nếu có
y = data["Function"]  # Cột nhãn

# Tiến hành tiêu chuẩn hóa dữ liệu nếu cần
# Ví dụ: sử dụng StandardScaler từ sklearn để tiêu chuẩn hóa dữ liệu
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Kiểm tra kích thước của dữ liệu
print("Shape of X_train:", X_train.shape)
print("Shape of X_test:", X_test.shape)
print("Shape of y_train:", y_train.shape)
print("Shape of y_test:", y_test.shape)
