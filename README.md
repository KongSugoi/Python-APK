Chạy thuật toán Forest Random
+ Chạy ở file trainandtest
+ Sửa path file csv thành path file csv cuối cùng chứa các sample dưới dạng
+ Dòng 1 chứa
  feature1, feature2, feature3, ..., lable
+ Các dòng tiếp theo là các sample dưới dạng 1 vector với giá trị các feature tương ứng với hàm 1
  *** Lưu ý: nên để 50% begin và 50% malware xen kẽ nhau
+ Output: tính accuracy dựa vào 20% sample trong file train để test phân loại xem đúng hay không.
+ Có thể thêm các param sau để tăng accuracy:  RandomForest(n_trees = số cây trong rừng, min_samples_split: số mẫu tối thiểu trong node)
  
