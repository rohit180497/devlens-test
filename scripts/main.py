from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="scripts/frontend/static"), name="static")

@app.get("/", response_class=HTMLResponse)
def login_page():
    with open("scripts/frontend/login.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    # Dummy authentication logic
    if username == "admin" and password == "password":
        return RedirectResponse(url="/welcome", status_code=303)
    return HTMLResponse("<h3>Login failed. <a href='/'>Try again</a></h3>")

@app.get("/welcome", response_class=HTMLResponse)
def welcome():
    return "<h2>Welcome, admin!</h2>"

if __name__ == "__main__":
    uvicorn.run("scripts.main:app", host="127.0.0.1", port=8000, reload=True)
