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

```python other_fcg.py```

<p> Code sẽ chạy và tạo ra 1 file csv chứa các thông tin về các hàm và tọa độ của các hàm trên đồ thị</p>
<p> Nếu không có thư viện nào sử dụng pip install để add thêm thư viện</p>

## Code Doc2vec

<p> Thực hiện tải thư viện gensim</p>

```pip install gensim```
<p> Thực hiện training và tạo model doc2vec</p>

```python train_doc2vec.py```
<p> Code sẽ tạo ra 1 file model để train doc2vec </p>
<p> Thực hiện chỉnh sử đường dẫn là folder chứa các file java</p>

<p> Run code </p>

```python doc2vec.py```

<p>Chương trình sẽ tạo ra 1 file csv chứa các hàm đã được dán nhãn và từ đây sẽ đưa vào cnn để thực hiện nhúng vào 1 vector chung</p>
