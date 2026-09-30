import json
import os
from main import SessionLocal, ResourceDB, engine, Base

def load_data():
    # Ensure database schema is created
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    file_path = './data/nmp.json'
    if not os.path.exists(file_path):
        print(f"Error: Could not find {file_path}")
        return

    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
            
        count = 0
        for item in data:
            resource = ResourceDB(
                title=item.get('標題', ''),
                author=item.get('作者', ''),
                publisher=item.get('出版單位', ''),
                publish_date=item.get('出版年月', ''),
                isbn=item.get('ISBN', '').strip(),
                source_url=item.get('資料來源網址', '').strip()
            )
            db.add(resource)
            count += 1
        
        db.commit()
        print(f"Successfully loaded {count} records into the database.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    load_data()
