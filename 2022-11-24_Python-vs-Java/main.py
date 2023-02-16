from fastapi import FastAPI
from pydantic import BaseModel as Schema, validator

app = FastAPI()


@app.get('/')
async def index():
    return {'msg': 'hello'}


@app.get('/hello')
async def hello(firstname: str, lastname: str):
    return {'msg': f'hello {firstname} {lastname}'}


class UserLoginSchema(Schema):
    username: str
    password: str

    @validator('password', pre=True)
    def password_validator(cls, password):
        if '$' in password:
            raise ValueError('Invalid character in password')
        return password


@app.post('/login')
async def login(user: UserLoginSchema):
    return {'msg': f'Logged-in {user.username}'}



# uruchamianie:
# uvicorn main:app