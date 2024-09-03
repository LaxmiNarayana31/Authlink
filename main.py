from fastapi.staticfiles import StaticFiles
import uvicorn
import os
from fastapi import FastAPI
from config.database import engine, Base
from config.database import SessionLocal
from fastapi_pagination import add_pagination
from app.modules.user import user_route
from app.modules.login import login_route
from app.modules.forgot_password import forget_password_route
from app.modules.company import company_routes
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

add_pagination(app)


Base.metadata.create_all(bind = engine)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

session = SessionLocal()

@app.get("/")
def welcome():
    return {"message": "Welcome to the FastAPI Project"}

app.include_router(login_route.router)
app.include_router(user_route.router)
app.include_router(company_routes.router)
app.include_router(forget_password_route.router)



if __name__ == '__main__':
    host_ip = os.getenv('HOST_IP', '127.0.0.1')  # Use default '127.0.0.1' if HOST_IP is not found
    port = int(os.getenv('PORT', 8000))  
    uvicorn.run("main:app", host = host_ip, port = port, log_level = "info", reload = True)

    print("running")

