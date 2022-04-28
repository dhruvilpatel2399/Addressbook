from sqlalchemy.orm import Session

from . import models, schemas

def get_address(db: Session , name:str):
    return db.query(models.Address).filter(models.Address.name == name).first()

def get_address_by_coordinate(db:Session, latitude:float, longitude:float):
    latt=latitude+0.001
    latb=latitude-0.001
    lont=longitude+0.001
    lonb=longitude-0.001

    return db.query(models.Address).filter(models.Address.latitude>=latb,
                                            models.Address.latitude<=latt,
                                            models.Address.longitude>=lonb,
                                            models.Address.longitude<=lont).all()

def create_address(db:Session, address:schemas.AddressBase):
    new_address=models.Address(name=address.name,
                                address=address.address,
                                longitude=address.longitude,
                                latitude=address.latitude)
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return {"message":"Address Inserted Successfully"}

def update_address(db:Session, name, address, latitude, longitude):
    update_addr=db.query(models.Address).filter(models.Address.name == name).first()
    
    update_addr.name=name
    update_addr.address=address 
    update_addr.latitude=latitude
    update_addr.longitude=longitude

    db.flush()
    db.commit()
    db.refresh(update_addr)

    return {"message":"Address updated Successfully"}

 
def delete_address(db:Session, name):
    del_name=get_address(db,name)
    db.delete(del_name)
    db.commit()
    {"message":"Address deleted Successfully"}
    





# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
