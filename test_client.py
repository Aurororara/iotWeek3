import requests

BASE_URL = "http://127.0.0.1:8000"

def run_tests():
    print("--- 1. 測試 CREATE (POST) ---")
    new_data = {
        "title": "測試新增的書籍",
        "author": "AI 開發者",
        "publisher": "國立臺北商業大學",
        "publish_date": "202410",
        "isbn": "1234567890",
        "source_url": "https://example.com"
    }
    response = requests.post(f"{BASE_URL}/resources/", json=new_data)
    print("Response Status Code:", response.status_code)
    print("Response JSON:", response.json())
    created_id = response.json().get("id")
    print("\n")

    print("--- 2. 測試 READ 列表 (GET) ---")
    response = requests.get(f"{BASE_URL}/resources/?limit=5")
    print("Response Status Code:", response.status_code)
    print(f"取得 {len(response.json())} 筆資料 (僅顯示前兩筆):")
    print(response.json()[:2])
    print("\n")

    if created_id:
        print(f"--- 3. 測試 READ 單筆 (GET) ID={created_id} ---")
        response = requests.get(f"{BASE_URL}/resources/{created_id}")
        print("Response Status Code:", response.status_code)
        print("Response JSON:", response.json())
        print("\n")

        print(f"--- 4. 測試 UPDATE (PUT) ID={created_id} ---")
        update_data = new_data.copy()
        update_data["title"] = "測試新增的書籍 (已更新)"
        response = requests.put(f"{BASE_URL}/resources/{created_id}", json=update_data)
        print("Response Status Code:", response.status_code)
        print("Response JSON:", response.json())
        print("\n")

        print(f"--- 5. 測試 DELETE (DELETE) ID={created_id} ---")
        response = requests.delete(f"{BASE_URL}/resources/{created_id}")
        print("Response Status Code:", response.status_code)
        print("刪除完成\n")

if __name__ == "__main__":
    try:
        requests.get(BASE_URL)
        run_tests()
    except requests.exceptions.ConnectionError:
        print(f"錯誤：無法連線到 {BASE_URL}，請確認 FastAPI 伺服器是否已經啟動！")
        print("請在另一個終端機執行：uvicorn main:app --reload")
