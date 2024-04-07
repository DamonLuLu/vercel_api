from fastapi import FastAPI
# from mangum import Mangum
import uvicorn
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# handler = Mangum(app)
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1",workers=1)
