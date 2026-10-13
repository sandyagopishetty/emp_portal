from pathlib import Path

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import FileResponse

app = FastAPI(title="Employee Portal")

BASE_DIR = Path(__file__).parent

employees = []
departments = []

class Employee(BaseModel):
    employee_id: str
    name: str
    salary: float
    department: str
class Department(BaseModel):
    department_id: str
    department_name: str


@app.get("/health")
def health():
    return "health is good"

@app.get("/home")
def home():
    return FileResponse(BASE_DIR / "index.html")

@app.get("/employees")
def get_employee():
    return employees

@app.post("/employees")
def add_employee(emp: Employee):
    employees.append(emp.model_dump())
    return emp
@app.get("/departments")
def get_department():
    return departments

@app.post("/departments")
def add_department(dept: Department):
    departments.append(dept.model_dump())
    return dept





if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)