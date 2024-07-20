from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

import crud, models
from db import SessionLocal, engine


from cities import suggest_city as suggest
from weather import get_forecast 

models.Base.metadata.create_all(bind=engine)


app = FastAPI()
templates = Jinja2Templates(directory='templates')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
async def root(request: Request, db: Session = Depends(get_db)):
    user = crud.get_or_create_user(db, request.client.host)
    cities_instance = crud.get_all_cities(db)
    if user.last_city_id == -1:
        last_city = ''
    else:
        last_city = crud.get_city_by_id(db, user.last_city_id).name
    
    history = [city.name for city in user.cities][::-1]
    context = {
        'request': request,
        'last_city_name': last_city,
        'history': history,
        'cities': cities_instance
    }

    return templates.TemplateResponse('root.html', context=context)


@app.get('/suggest_city')
async def suggest_city(city: str):
    suggestions = await suggest(city)
    return {'suggestions': suggestions}

@app.get('/forecast')
async def forecast(request: Request, lat: float, lon: float, city_name: str, fias_id: str, db: Session = Depends(get_db)):
    user = crud.get_or_create_user(db, request.client.host)
    city = crud.get_or_create_city(db=db, name=city_name, lat=lat, lon=lon, fias_id=fias_id)
    user.cities.append(city)
    user.last_city_id = city.id
    db.add(user)
    db.commit()

    resp = get_forecast(user_ip=request.client.host)
    return resp