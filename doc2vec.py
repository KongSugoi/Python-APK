from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import os

# Hàm để đọc các hàm từ file và gán nhãn cho chúng
def read_java_files(folder_path):
    documents = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    documents.append(TaggedDocument(content.split(), [file_path]))  # Gán nhãn cho mỗi tài liệu
    return documents

# Đường dẫn tới thư mục chứa các file mã nguồn Java
folder_path = "D:\BTL_PYTHON\Output_file"

# Đọc các hàm từ các file và gán nhãn cho chúng
documents = read_java_files(folder_path)

# Xây dựng mô hình Doc2Vec
model = Doc2Vec(documents, vector_size=100, window=5, min_count=1, workers=4)

# Lưu mô hình vào tệp model.txt
model.save("model.txt")

# Lấy vector của một tài liệu cụ thể (ví dụ: tài liệu thứ 0)
vector = model.infer_vector(documents[1].words)
print("Vector of document 1:", vector)
