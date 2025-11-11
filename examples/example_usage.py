import json
from pathlib import Path
import sys

def load_data():
    """Tải dữ liệu từ file dataset.json ở thư mục gốc."""
    try:
        # Lấy đường dẫn thư mục gốc
        ROOT_DIR = Path(__file__).parent.parent
        DATA_FILE = ROOT_DIR / 'dataset.json'
        
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{DATA_FILE.name}'. Đảm bảo file này nằm ở thư mục gốc.", file=sys.stderr)
        return None
    except json.JSONDecodeError:
        print(f"Lỗi: File '{DATA_FILE.name}' có định dạng JSON không hợp lệ.", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Đã xảy ra lỗi không xác định: {e}", file=sys.stderr)
        return None

def query_example_1(data, disease_name):
    """Ví dụ 1: Tìm tất cả thuốc hóa học trị một bệnh cụ thể."""
    print(f"--- VÍ DỤ 1: TÌM THUỐC TRỊ BỆNH '{disease_name}' ---")
    
    found_disease = None
    for disease in data.get('diseases', []):
        if disease['disease_name'] == disease_name:
            found_disease = disease
            break
            
    if found_disease:
        chemicals = found_disease.get('treatment_chemicals', [])
        if not chemicals:
            print(f"Không tìm thấy thuốc hóa học nào cho '{disease_name}' trong CSDL.")
            return

        print(f"Đã tìm thấy {len(chemicals)} loại thuốc/hoạt chất cho '{disease_name}':\n")
        for chem in chemicals:
            print(f"  Tên thương mại: {chem.get('name', 'N/A')}")
            print(f"  Hoạt chất: {chem.get('active_ingredient', 'N/A')}")
            print(f"  Loại thuốc: {chem.get('type', 'N/A')}")
            print(f"  Cách dùng: {chem.get('application_method', 'N/A')}")
            print("-" * 20)
    else:
        print(f"Không tìm thấy bệnh có tên '{disease_name}'")

def query_example_2(data, season):
    """Ví dụ 2: Tìm tất cả các bệnh và sâu hại bùng phát vào MÙA KHÔ."""
    print(f"\n--- VÍ DỤ 2: TÌM CÁC VẤN ĐỀ BÙNG PHÁT VÀO '{season}' ---")
    
    results = []

    # Tìm trong diseases
    for disease in data.get('diseases', []):
        if season in disease.get('risk_season', []):
            results.append(f"[BỆNH] {disease['disease_name']}")

    # Tìm trong pests
    for pest in data.get('pests', []):
        if season in pest.get('risk_season', []):
            results.append(f"[SÂU HẠI] {pest['pest_name']}")
            
    if results:
        print(f"Đã tìm thấy {len(results)} vấn đề bùng phát vào '{season}':\n")
        for res in results:
            print(f"  - {res}")
    else:
        print(f"Không tìm thấy vấn đề nào bùng phát vào '{season}'.")

def main():
    """Hàm chính để chạy các ví dụ."""
    data = load_data()
    
    if data:
        # In thông tin metadata
        metadata = data.get('metadata', {})
        print(f"Đã tải thành công CSDL: {metadata.get('name')}")
        print(f"Phiên bản: {metadata.get('version')}\n")
        
        # Chạy các ví dụ truy vấn
        query_example_1(data, "Bệnh Xì Mủ Thân (Nứt Thân)")
        query_example_2(data, "mùa khô")

if __name__ == "__main__":
    main()