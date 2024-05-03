from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import csv
import os

# Đường dẫn tới file mô hình đã lưu
model_path = "doc2vec_model"

# Kiểm tra xem file mô hình đã tồn tại hay chưa
if os.path.exists(model_path):
    # Load mô hình đã tồn tại
    model = Doc2Vec.load(model_path)
else:
    # Tạo một mô hình mới nếu chưa tồn tại
    model = Doc2Vec(vector_size=100, window=5, min_count=1, workers=4, epochs=20)

# Đọc dữ liệu từ file CSV và thêm vào danh sách documents
data = []
with open("fcg_coordinates.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

# Biểu diễn dữ liệu theo định dạng phù hợp cho doc2vec
new_documents = [TaggedDocument(doc, [i + model.corpus_count]) for i, doc in enumerate(data)]

# Kiểm tra xem biến documents đã được định nghĩa hay chưa
if 'documents' in locals():
    # Nếu biến documents đã tồn tại, thêm dữ liệu mới vào danh sách documents
    documents.extend(new_documents)
else:
    # Nếu biến documents chưa được định nghĩa, gán danh sách new_documents cho biến documents
    documents = new_documents

# Cập nhật từ vựng và huấn luyện mô hình
model.build_vocab(documents, update=True)
model.train(documents, total_examples=model.corpus_count, epochs=model.epochs)

# Lưu mô hình đã được cập nhật
model.save(model_path)
