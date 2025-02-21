from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class DataRequest(BaseModel):
    data: List[str]

@app.post("/bfhl")
async def process_data(request: DataRequest):
    numbers = []
    alphabets = []

    for item in request.data:
        if item.isdigit():
            numbers.append(item)
        else:
            alphabets.append(item)

    response = {
        "status": "success",
        "user_id": "abhay_kumar_21022025",
        "college_email": "22bcs13112@cuchd.in",
        "college_roll_number": "13112",
        "array_for_numbers": numbers,
        "array_for_alphabets": alphabets,
        "is_success": True
    }
    return response

@app.get("/bfhl")
async def get_operation_code():
    return {"operation_code": 1}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)