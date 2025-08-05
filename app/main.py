from fastapi import FastAPI


app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/version")
async def version():
    return {"version": "1.0.0"}     

@app.get("/query")
async def query():
    return {"message": "Query endpoint"}

@app.get("/search")
async def search():
    return {"message": "Search endpoint"}       

@app.get("/upload")
async def upload():
    return {"message": "Upload endpoint"}

main = app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# app/main.py

