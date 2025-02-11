from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database.movies import Movies
from setup import get_db


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

class  MovieData(BaseModel):
    name: str
    time: int
    show: str
    price: float

@app.post("/check_movies")
def enter_movie(input_movie: MovieData, db: Session = Depends(get_db)):
    db_movies = Movies(
        name=input_movie.name,
        show=input_movie.show,
        time=input_movie.time,
    )
    db.add(db_movies)
    db.commit()
    db.refresh(db_movies)
    return db_movies

@app.get("/getmovies")
def fetch_movies(db : Session = Depends(get_db)):
    movie = db.query(Movies).all()
    return movie

@app.delete("/delete_movie/{movie_id}")
def delete_data(movie_id:int, db:Session = Depends(get_db)):
    movie = db.query(Movies).filter(Movies.id == movie_id).first()
    db.delete(movie)
    db.commit()
    return "movie deleted"

@app.put("/update_movie/{movie_id}")
def update_data(movie_id:int, movie_new: MovieData, db:Session = Depends(get_db)):
    movie = db.query(Movies).filter(Movies.id == movie_id).first()
    movie.name= movie_new.name
    movie.show= movie_new.show
    movie.price= movie_new.price
    movie.time= movie_new.time
    db.commit()
    db.refresh(movie)
    return movie


