import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv1D, MaxPooling1D, Flatten

# Đọc dữ liệu từ file CSV
data = pd.read_csv("vectors.csv")

# Biến đổi dữ liệu thành mảng numpy
X = data.drop(columns=["Function"]).values

# Xây dựng mạng neural network (CNN)
model = Sequential()
model.add(Conv1D(64, 3, activation='relu', input_shape=(X.shape[1], 1)))  # Tầng Convolutional với 64 bộ lọc kích thước 3 và hàm kích hoạt relu
model.add(MaxPooling1D(2))  # Tầng MaxPooling
model.add(Flatten())  # Định hình lại thành vector 1 chiều
model.add(Dense(128, activation='relu'))  # Tầng kết nối đầy đủ với 128 đơn vị ẩn và hàm kích hoạt relu
model.add(Dense(1, activation='sigmoid'))  # Tầng kết nối đầy đủ cuối cùng với 1 đơn vị đầu ra và hàm kích hoạt sigmoid (binary classification)

# Biên soạn mô hình
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Nhúng dữ liệu từ file CSV bằng mạng neural network
embedded_vectors = model.predict(X.reshape(X.shape[0], X.shape[1], 1))

# Tạo DataFrame từ kết quả nhúng
embedded_df = pd.DataFrame(embedded_vectors, columns=[f"Vector_{i}" for i in range(embedded_vectors.shape[1])])

# Thêm cột "Function" vào DataFrame
embedded_df["Function"] = data["Function"]

# Lưu kết quả nhúng vào file CSV
embedded_df.to_csv("D:\BTL_PYthon\CNN\embedded_vectors_17.csv", index=False)
