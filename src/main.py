from fastapi import FastAPI
from routes.views import routingMap
app = FastAPI(title="Desafio transfeera api")
@app.get("/")
def root():
  return {"Bem vindo a tranfeera api"}

routingMap.create(app)
