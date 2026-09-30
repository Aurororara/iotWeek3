from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, Field
from typing import List, Optional

# Database setup
DATABASE_URL = "sqlite:///./nmp_data.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy Model
class ResourceDB(Base):
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    publisher = Column(String)
    publish_date = Column(String)
    isbn = Column(String)
    source_url = Column(String)

Base.metadata.create_all(bind=engine)

# Pydantic Models for API
class ResourceBase(BaseModel):
    title: str = Field(..., description="標題")
    author: Optional[str] = Field(None, description="作者")
    publisher: Optional[str] = Field(None, description="出版單位")
    publish_date: Optional[str] = Field(None, description="出版年月")
    isbn: Optional[str] = Field(None, description="ISBN")
    source_url: Optional[str] = Field(None, description="資料來源網址")

class ResourceCreate(ResourceBase):
    pass

class Resource(ResourceBase):
    id: int
    
    # For Pydantic v2 compatibility
    model_config = {"from_attributes": True}

app = FastAPI(
    title="NMP Open Data API",
    description="臺東南島文化節 國立臺灣史前文化博物館圖書資料 CRUD API",
    version="1.0.0"
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/resources/", response_model=Resource, status_code=201, tags=["Resources"])
def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    db_resource = ResourceDB(**resource.model_dump())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

@app.get("/resources/", response_model=List[Resource], tags=["Resources"])
def read_resources(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    resources = db.query(ResourceDB).offset(skip).limit(limit).all()
    return resources

@app.get("/resources/{resource_id}", response_model=Resource, tags=["Resources"])
def read_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = db.query(ResourceDB).filter(ResourceDB.id == resource_id).first()
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource

@app.put("/resources/{resource_id}", response_model=Resource, tags=["Resources"])
def update_resource(resource_id: int, resource: ResourceCreate, db: Session = Depends(get_db)):
    db_resource = db.query(ResourceDB).filter(ResourceDB.id == resource_id).first()
    if db_resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    for key, value in resource.model_dump().items():
        setattr(db_resource, key, value)
    db.commit()
    db.refresh(db_resource)
    return db_resource

@app.delete("/resources/{resource_id}", status_code=204, tags=["Resources"])
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    db_resource = db.query(ResourceDB).filter(ResourceDB.id == resource_id).first()
    if db_resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    db.delete(db_resource)
    db.commit()
    return None
