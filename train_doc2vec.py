from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import csv

# Đọc dữ liệu từ file CSV
data = []
with open("fcg_coordinates.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

# Biểu diễn dữ liệu theo định dạng phù hợp cho doc2vec
documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(data)]

# Huấn luyện mô hình doc2vec
model = Doc2Vec(vector_size=100, window=5, min_count=1, workers=4, epochs=20)
model.build_vocab(documents)
model.train(documents, total_examples=model.corpus_count, epochs=model.epochs)

# Lưu mô hình doc2vec
model.save("doc2vec_model")
