from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from read_csv import read_csv  # import to read csv file

app = FastAPI()

# CORS Origins
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

# Set up CORS to allow front end and back end to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# REST API endpoint to verify CORS is working
@app.get("/")
async def root():
    return {"message": "Hello World"}

# REST API endpoint to get test data
@app.get("/get_daily_test_data")
async def get_daily_test_data():
    try:
        data = read_csv()  # Make sure read_csv() doesn't crash
        return JSONResponse(content=data)
    except Exception as e:
        print("Error reading CSV:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)

