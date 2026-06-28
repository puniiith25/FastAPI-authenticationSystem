from fastapi import FastAPI
from pydantic import  BaseModel
import json
import os
app = FastAPI()

@app.get('/')
def health():
    return "server is running"

def saveuser(user):
    with open('user.json','w') as file:
        json.dump(user ,file ,indent=4)
# data loader
# data loader# data loader

def loaduser():
    if not os.path.exists("user.json"):
        with open("user.json", "w") as file:
            json.dump([], file)
    with open('user.json','r') as file:
        return  json.load( file)
class UserRegister(BaseModel):
    name:str
    email:str
    password:str
@app.post('/register')
def register(user:UserRegister):
    users = loaduser()
    for u in users:
        if u['email'] == user.email :
            return "user already exists"
    users.append({
        "name":user.name,
        "email":user.email,
        "password":user.password

    })
    saveuser(users)
    return {"message":f"{user.email} Registered Successfully"}

class UserLogin(BaseModel):
    email:str
    password: str
@app.post('/login')
def login(user:UserLogin):
    users = loaduser()
    for u in users:
        if u['email'] == user.email:
            if u['password'] == user.password:
                return {"message":f"{user.email} loged in successfully"}

            return {"message": "wrong password"}

    return {"message": "user user not found"}


@app.get('/users')
def allusers():
    return {"Users":loaduser()}
