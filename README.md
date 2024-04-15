## Tải File APK về máy 

<p> Sử dụng adrozoo, chỉnh sửa đường dẫn là file begin.txt, số lượng mã hash trong file là số lượng file apk tải về. lựa chọn đường dẫn lưu file apk </p>

## Xử lý decompile qua androguard

<p> Thực hiện tải androguard phiên bản 3.4 (Yêu cầu Python 3.11.4)</p>

```pip install androguard==3.4```

<p> Sử dụng lệnh </p>

```androguard decompile <tên file> -o <tên folder output> ```

<p> Nhận được 1 folder các gồm các file java và các file thư viện</p>

## Code FCG 

<p> Thực hiện chỉnh sửa đường dẫn là folder chứa các file java</p>

<p> Run code </p>

```python function_call_graph.py```

<p> Code sẽ chạy và tạo ra 1 đồ thị các hàm và liên kết giữa các hàm</p>
<p> Nếu không có thư viện nào sử dụng pip install để add thêm thư viện</p>

## Code Doc2vec

<p> Thực hiện tải thư viện gensim</p>

```pip install gensim```

<p> Thực hiện chỉnh sử đường dẫn là folder chứa các file java</p>

<p> Run code </p>

```python doc2vec.py```

<p> Chương trình sẽ tạo ra kết quả là hệ thống model của mỗi nhãn document, tương ứng với 1 hàm</p>
