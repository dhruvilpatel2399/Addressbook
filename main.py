from typing import Optional

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

from sql_app.crud import create_address, delete_address, get_address, get_address_by_coordinate, delete_address, update_address
from sql_app.database import SessionLocal, engine
from sqlalchemy.orm import Session

from sql_app import schemas, models, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

'''
Endpoint to create Address
It will take following arguements:
name:dhruvil
address:123 parklane
longitude:50.0
latitude:50.0
'''
@app.post("/create/")
def create(item:schemas.AddressBase, db:Session = Depends(get_db)):
    addr=create_address(db, item)
    return addr

'''
Endpoint to search address based on name 
It will take name as arguement and will return address
'''
@app.post("/search-name/")
def search_name(name:str, db:Session = Depends(get_db)):
    return get_address(db, name)

'''
Endpoint to search address based on coordinate
it will take latitude and longitude and will return address
'''
@app.post("/search-coordinate/")
def search_coordinate(latitude:float, longitude:float, db:Session = Depends(get_db)):
    return get_address_by_coordinate(db,latitude,longitude)

'''
Endpoint to update address using Name
It will update address on the basis of name 
we can update latitude, longitude, address
'''
@app.post("/update/")
def update(name:str, address:str, latitude:float, longitude:float, db:Session=Depends(get_db)):
    return update_address(db, name, address, latitude, longitude)

'''
Endpoint to delete address by passing name
'''
@app.post("/delete/")
def delete(name:str, db:Session = Depends(get_db)):
    return delete_address(db, name)
