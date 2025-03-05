# Thuật toán tối ưu GWO-GA

## Giới thiệu

Dự án này triển khai thuật toán tối ưu lai giữa Grey Wolf Optimizer (GWO) và Genetic Algorithm (GA) để giải quyết các bài toán tối ưu hàm thử nghiệm. Hệ thống sẽ chạy các thuật toán, lưu kết quả fitness vào các file CSV, sau đó gộp dữ liệu lại để phân tích.

## Clone repository

Để tải về source code, chạy lệnh sau:

```bash
git clone <link-repo>
```

## 1. Cài đặt thư viện cần thiết

Trước khi chạy chương trình, cần cài đặt các thư viện Python yêu cầu bằng lệnh:

```bash
pip install numpy pandas matplotlib
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
