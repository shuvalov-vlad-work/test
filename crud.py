from sqlalchemy.orm import Session

import models

def get_or_create_user(db: Session, user_ip: str):
    instance = db.query(models.User).filter(models.User.ip == user_ip).first()
    if instance:
        return instance
    else:
        instance = models.User(ip = user_ip)
        db.add(instance)
        db.commit()
        db.refresh(instance)
        return instance

def get_or_create_city(db: Session, fias_id: str, name: str, lat: float, lon: float):
    instance = db.query(models.City).filter( 
        models.City.fias_id == fias_id
        ).first()
    all_cities = db.query(models.City).all()
    fc = db.query(models.City).filter( 
        models.City.lat == lat,
        models.City.lon == lon
        ).all()
    print()
    print(' ---------- ')
    print(lat, lon)
    #print([f'{i.name} {i.lat}' for i in all_cities])
    #print([f'{i.name} {i.lat}' for i in fc])
    print(instance)
    print(' ---------- ')
    print()
    if instance:
        instance.cnt += 1
        db.commit()
        return instance
    else:
        instance = models.City(
            name = name, 
            fias_id = fias_id,
            lat = lat,
            lon = lon,
            cnt = 1
            )
        db.add(instance)
        db.commit()
        db.refresh(instance)
        return instance
    
def get_city_by_id(db: Session, city_id: int):
    instance = db.query(models.City).filter(
        models.City.id == city_id
    ).first()
    return instance

def get_all_cities(db: Session):
    instance = db.query(models.City).order_by(models.City.cnt.desc()).limit(10).all()
    return instance