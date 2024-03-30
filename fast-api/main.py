from typing import Union, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class MathOperation(BaseModel):
    num1: Union[float, int]
    num2: Union[float, int]



class MathResult(BaseModel):
    result: Union[float, int]



@app.post("/add", response_model=MathResult, status_code=201)
def add_numbers(operation: MathOperation):
    result = operation.num1 + operation.num2
    return {"result": result}


@app.post("/subtract", response_model=MathResult, status_code=201)
def subtract_numbers(operation: MathOperation):
    result = operation.num1 - operation.num2
    return {"result": result}


@app.post("/multiply", response_model=MathResult, status_code=201)
def multiply_numbers(operation: MathOperation):
    result = operation.num1 * operation.num2
    return {"result": result}


@app.post("/divide", response_model=MathResult, status_code=201)
def divide_numbers(operation: MathOperation):
    if operation.num2 == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    result = operation.num1 / operation.num2
    return {"result": result}
