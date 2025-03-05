# Thuật toán tối ưu GWO-GA

## Giới thiệu

Dự án này phát triển một phương pháp tối ưu hóa lai giữa Grey Wolf Optimizer (GWO) và Genetic Algorithm (GA), kết hợp với chiến lược tinh chỉnh cực trị địa phương (CLS) để cải thiện khả năng tìm kiếm nghiệm tối ưu. Hệ thống sẽ thực thi các thuật toán, ghi lại giá trị fitness vào các file CSV và tổng hợp dữ liệu để phân tích.

## Khởi tạo môi trường ảo

Trước khi cài đặt các thư viện, bạn cần tạo một môi trường ảo để quản lý các thư viện Python. Chạy các lệnh sau:

```bash
# Tạo môi trường ảo
python -m venv venv

# Kích hoạt môi trường ảo
# Trên Windows
.\venv\Scripts\activate

# Trên macOS/Linux
source venv/bin/activate
```

## Clone repository

Để tải về source code, chạy lệnh sau:

```bash
https://github.com/nguyendevwk/GWO-GA-CLS.git
```

## 1. Cài đặt thư viện cần thiết

Trước khi chạy chương trình, cần cài đặt các thư viện Python yêu cầu bằng lệnh:

```bash
pip install -r requirements.txt
```

## 2. Cấu trúc thư mục

```
GWO-GA-CLS/
│── dim10/
│── dim30/
│── dim50/
│── venv/
│── app.py
│── benchmark.py
│── combined_functions_10.csv
│── genetic_algorithm.py
│── grey_wolf_genetic_algorithm.py
│── grey_wolf_optimizer.py
│── quay.py
```

## 3. Chạy thuật toán

Chạy `app.py` để thực thi các thuật toán và lưu kết quả fitness:

```bash
python app.py
```

Sau khi chạy xong, chương trình sẽ lưu kết quả fitness vào các file CSV trong thư mục `dim10/`, `dim30/`, `dim50/` tùy vào kích thước bài toán.

## 4. Gộp dữ liệu sau khi chạy thuật toán

Sau khi chạy thuật toán và có các giá trị fitness được lưu, tiếp tục chạy `quay.py` để gộp dữ liệu lại thành một file CSV tổng hợp:

```bash
python quay.py
```

File `combined_functions_10.csv` sẽ được tạo ra, chứa dữ liệu tổng hợp theo từng hàm thử nghiệm.

## 5. Ghi chú

-   Có thể thay đổi kích thước của bài toán bằng cách chỉnh sửa biến `dim` trong `quay.py`.
-   Đảm bảo rằng tất cả các file đầu vào có sẵn trong thư mục tương ứng trước khi chạy `quay.py`.
