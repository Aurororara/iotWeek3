# NMP Open Data API 規格與文件 (API Documentation)

本文件描述了以 FastAPI 實作之「國立臺灣史前文化博物館圖書資料」RESTful API 的詳細規格與實測範例。
您也可以直接啟動伺服器，並前往 `http://127.0.0.1:8000/docs` 查看互動式的 Swagger UI 文件。

---

## 1. 取得圖書資料列表 (Read Multiple)

- **Method**: `GET`
- **URL Path**: `/resources/`
- **Query Parameters**:
  - `skip` (整數, 預設為 0)
  - `limit` (整數, 預設為 100)

### 實測範例
**API Request**:
```http
GET /resources/?limit=2 HTTP/1.1
Host: 127.0.0.1:8000
```

**API Response**:
- **Status Code**: `200 OK`
- **Output (JSON)**:
```json
[
  {
    "title": "南島民族樂器專刊 : 二○○二臺東南島文化節",
    "author": "吳榮順",
    "publisher": "東縣府",
    "publish_date": "09101",
    "isbn": "957013030X ",
    "source_url": "https://libm7.moc.gov.tw/webopac/dy.aspx?key=4&str=THM04BHC0024328&db=M7_nmp",
    "id": 1
  },
  {
    "title": "走過土地認識人民 : 台灣慣習記事資料彙編(I)",
    "author": "陳若雲",
    "publisher": "原民文化出版",
    "publish_date": "08801",
    "isbn": "9578491344 ",
    "source_url": "https://libm7.moc.gov.tw/webopac/dy.aspx?key=4&str=THM04BHC0030502&db=M7_nmp",
    "id": 2
  }
]
```

---

## 2. 新增圖書資料 (Create)

- **Method**: `POST`
- **URL Path**: `/resources/`

### 實測範例
**API Request**:
```http
POST /resources/ HTTP/1.1
Host: 127.0.0.1:8000
Content-Type: application/json

{
  "title": "測試新增書籍",
  "author": "AI開發者",
  "publisher": "臺北商業大學",
  "publish_date": "202410",
  "isbn": "1234567890",
  "source_url": "https://example.com"
}
```

**API Response**:
- **Status Code**: `201 Created`
- **Output (JSON)**:
```json
{
  "title": "測試新增書籍",
  "author": "AI開發者",
  "publisher": "臺北商業大學",
  "publish_date": "202410",
  "isbn": "1234567890",
  "source_url": "https://example.com",
  "id": 100
}
```

---

## 3. 取得單筆圖書資料 (Read Single)

- **Method**: `GET`
- **URL Path**: `/resources/{id}`

### 實測範例
**API Request**:
```http
GET /resources/100 HTTP/1.1
Host: 127.0.0.1:8000
```

**API Response**:
- **Status Code**: `200 OK`
- **Output (JSON)**:
```json
{
  "title": "測試新增書籍",
  "author": "AI開發者",
  "publisher": "臺北商業大學",
  "publish_date": "202410",
  "isbn": "1234567890",
  "source_url": "https://example.com",
  "id": 100
}
```

---

## 4. 更新圖書資料 (Update)

- **Method**: `PUT`
- **URL Path**: `/resources/{id}`

### 實測範例
**API Request**:
```http
PUT /resources/100 HTTP/1.1
Host: 127.0.0.1:8000
Content-Type: application/json

{
  "title": "測試新增書籍 (已更新版)",
  "author": "AI開發者",
  "publisher": "臺北商業大學",
  "publish_date": "202411",
  "isbn": "1234567890",
  "source_url": "https://example.com"
}
```

**API Response**:
- **Status Code**: `200 OK`
- **Output (JSON)**:
```json
{
  "title": "測試新增書籍 (已更新版)",
  "author": "AI開發者",
  "publisher": "臺北商業大學",
  "publish_date": "202411",
  "isbn": "1234567890",
  "source_url": "https://example.com",
  "id": 100
}
```

---

## 5. 刪除圖書資料 (Delete)

- **Method**: `DELETE`
- **URL Path**: `/resources/{id}`

### 實測範例
**API Request**:
```http
DELETE /resources/100 HTTP/1.1
Host: 127.0.0.1:8000
```

**API Response**:
- **Status Code**: `204 No Content`
- **Output**: *(無回傳內容)*
