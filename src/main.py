from fastapi import FastAPI
from routes.views import routingMap
app = FastAPI(title="Desafio api")
@app.get("/")
def root():
  return {"Bem vindo a api de pagamentos"}

routingMap.create(app)
