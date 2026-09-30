# IoTApp Week 3 - Open Data RESTful API

本專案使用 Python + FastAPI 實作了針對 [文化部開放資料 - 國立臺灣史前文化博物館圖書資料](https://libm7.moc.gov.tw/webopac/opendata/nmp.json) 的 RESTful API Server，提供完整 CRUD 服務。

## 系統需求
- Python 3.8+
- SQLite (內建)

## 安裝與環境建置

1. 建立並啟動虛擬環境 (建議)：
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# 或是 venv\Scripts\activate # Windows
```

2. 安裝相依套件：
```bash
pip install -r requirements.txt
```

## 執行步驟

1. **匯入 Open Data 資料到 SQLite 資料庫**
   執行以下指令，程式會讀取 `data/nmp.json` 並將資料寫入 SQLite 資料庫 `nmp_data.db` 中。
   ```bash
   python load_data.py
   ```

2. **啟動 FastAPI 伺服器**
   ```bash
   uvicorn main:app --reload
   ```
   伺服器啟動後，將運行於 `http://127.0.0.1:8000`

3. **查看線上 API 文件 (Swagger UI)**
   打開瀏覽器，前往：[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   這裡可以看到自動產生的 API 規格與文件，並且可以直接在網頁上測試 API。

4. **執行測試 Client (測試 CRUD)**
   開啟另一個終端機（確認已在同一個環境中），執行測試腳本，該腳本會自動發送 CRUD 的 Request 並印出 Response。
   ```bash
   python test_client.py
   ```

## 專案檔案結構
- `data/nmp.json`: Open Data 原始資料
- `main.py`: FastAPI 主程式，包含 DB Model 與 CRUD Endpoints
- `load_data.py`: 資料匯入腳本，用來將 JSON 塞入資料庫
- `test_client.py`: Python API Client 測試腳本
- `requirements.txt`: 專案相依套件列表
- `nmp_data.db`: SQLite 資料庫檔案 (執行 `load_data.py` 後產生)

## API 規格摘要 (CRUD)
- `POST /resources/` : Create (新增資料)
- `GET /resources/` : Read (取得列表)
- `GET /resources/{id}` : Read (取得單筆資料)
- `PUT /resources/{id}` : Update (更新單筆資料)
- `DELETE /resources/{id}` : Delete (刪除單筆資料)
