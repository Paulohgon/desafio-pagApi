from fastapi import FastAPI
from routes.views import routingMap
app = FastAPI()
@app.get("/")
async def root():
  return {"Bem vindo a tranfeera api"}

routingMap.create(app)
