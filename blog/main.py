from fastapi import FastAPI,Depends,status,Response
from . import schemas,models
from . database import engine,SessionLocal
from sqlalchemy.orm import Session



app = FastAPI()

models.Base.metadata.create_all(engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/task',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Task,db:Session=Depends(get_db)):
    new_task = models.Task(title=request.title,body=request.body)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.get('/task',status_code= status.HTTP_200_OK)
def all(db:Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return tasks

@app.get('/task/{id}')
def show(id,response:Response,db:Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id==id).first()
    if not task:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'details':f"Task with id {id} is mot found"}
    return task

@app.delete('/task/{id}',status_code= status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(get_db)):
    db.query(models.Task).filter(models.Task.id==id).delete(synchronize_session=False)
    db.commit()
    return 'Done'


@app.put('/task/{id}',status_code= status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Task,db:Session = Depends(get_db)):
    db.query(models.Task).filter(models.Task.id==id).update({'title':request.title,'body':request.body})
    db.commit()
    return 'updated'


