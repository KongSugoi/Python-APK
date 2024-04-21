from gensim.models.doc2vec import Doc2Vec
import csv

# Load mô hình doc2vec đã được huấn luyện trước
doc2vec_model = Doc2Vec.load("doc2vec_model")

# Đọc dữ liệu từ file CSV đã lưu các tọa độ của các hàm
coordinates = []
with open("fcg_coordinates.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Bỏ qua dòng tiêu đề
    for row in reader:
        coordinates.append(row)

# Nhúng dữ liệu thành các vector sử dụng doc2vec
vectors = []
for row in coordinates:
    function = row[0]
    x = float(row[1])
    y = float(row[2])
    vector = doc2vec_model.infer_vector([function, str(x), str(y)])
    vectors.append(vector)

# Lưu các vector vào một file CSV mới
output_file = "vectors.csv"
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Function"] + [f"Feature_{i}" for i in range(len(vectors[0]))])  # Tiêu đề
    for function, vector in zip(coordinates, vectors):
        writer.writerow([function[0]] + list(vector))

print("Các vector đã được lưu vào file:", output_file)
