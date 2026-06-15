import os
import pandas as pd
from sqlalchemy import create_engine

# ==========================================
# 1. CẤU HÌNH THÔNG TIN KẾT NỐI POSTGRESQL
# ==========================================
DB_USER = "postgres"         
DB_PASSWORD = "MatKhauMoi123" 
DB_HOST = "localhost"        # Giữ nguyên localhost
DB_PORT = "5432"             # Cổng mặc định
DB_NAME = "pds_chungkhoan"         # Tên database của bạn (để mặc định hoặc tên db bạn tự tạo)

# Tạo connection string
connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(connection_string)

# ==========================================
# 2. ĐỊNH NGHĨA ĐƯỜNG DẪN ĐẾN THƯ MỤC
# ==========================================
# Dùng tiền tố r"" để tránh lỗi dấu gạch chéo ngược (\) trong Windows
FOLDER_FACT = r"D:\Projects\Chứng khoán PDS\Fact"
FOLDER_DIM = r"D:\Projects\Chứng khoán PDS\Dim"

# ==========================================
# 3. HÀM XỬ LÝ VÀ UPLOAD FILE
# ==========================================
def upload_files_from_folder(folder_path, table_prefix=""):
    """
    Quét toàn bộ file trong thư mục, đọc dữ liệu và ghi vào PostgreSQL
    """
    if not os.path.exists(folder_path):
        print(f"❌ Thư mục không tồn tại: {folder_path}")
        return

    print(f"\n--- Đang xử lý thư mục: {folder_path} ---")
    
    # Lấy danh sách tất cả các file trong thư mục
    files = os.listdir(folder_path)
    
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        
        # Kiểm tra định dạng file (chấp nhận .csv và các định dạng Excel)
        if file_name.endswith(('.csv', '.xlsx', '.xls')):
            # Tự động lấy tên file làm tên bảng (ví dụ: Dim_Company)
            table_name = os.path.splitext(file_name)[0]
            # Chuẩn hóa tên bảng: chuyển thành chữ thường, thay khoảng trắng bằng dấu gạch dưới (nếu có)
            table_name = table_name.lower().replace(" ", "_")
            
            print(f"-> Đang đọc file: {file_name}...")
            
            try:
                # Đọc file dựa trên định dạng
                if file_name.endswith('.csv'):
                    # Đôi khi file từ Excel xuất ra dùng mã hóa utf-8 hoặc latin1/utf-8-sig
                    df = pd.read_csv(file_path, encoding='utf-8-sig')
                else:
                    df = pd.read_excel(file_path)
                
                # Chuẩn hóa tên các cột trong dataframe thành chữ thường để làm việc với Postgres dễ hơn
                df.columns = [col.lower().strip().replace(" ", "_") for col in df.columns]
                
                # Đẩy dữ liệu vào PostgreSQL
                # if_exists='replace': Nếu bảng đã có, xóa đi tạo lại bảng mới.
                # Nếu muốn ghi đè/chèn thêm dữ liệu vào bảng cũ thì đổi thành if_exists='append'
                df.to_sql(
                    name=table_name, 
                    con=engine, 
                    if_exists='replace', 
                    index=False, 
                    chunksize=5000 # Chia nhỏ dữ liệu để đẩy lên nhanh hơn nếu file lớn
                )
                print(f"   ✅ Đã upload thành công vào bảng: [{table_name}] ({len(df)} dòng)")
                
            except Exception as e:
                print(f"   ❌ Lỗi khi xử lý file {file_name}: {e}")

# ==========================================
# 4. CHẠY TIẾN TRÌNH UPLOAD
# ==========================================
if __name__ == "__main__":
    # 1. Upload các bảng Dim trước (vì thông thường các bảng Fact sẽ tham chiếu đến Dim)
    upload_files_from_folder(FOLDER_DIM)
    
    # 2. Upload các bảng Fact sau
    upload_files_from_folder(FOLDER_FACT)
    
    print("\n🎉 Hoàn thành toàn bộ quá trình ETL dữ liệu vào PostgreSQL!")