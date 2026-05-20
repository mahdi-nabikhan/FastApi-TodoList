from pydantic import BaseModel, Field
from typing import Optional

from datetime import datetime


class TaskBaseSchemas(BaseModel):
    title: str = Field(
        ..., max_length=150, min_length=5, description="Title of The Task"
    )
    description: Optional[str] = Field(
        ..., max_length=500, description="description of Task,"
    )
    is_complated: bool = Field(..., description="State of the Task")


class TaskCreateSchemas(TaskBaseSchemas):
    pass


class TaskUpateSchemas(TaskBaseSchemas):
    pass


class TaskResponseSchemas(TaskBaseSchemas):
    id: int = Field(..., description="unique identifier of the object")
    created_date: datetime = Field(..., description="Creations date and time of task")
    updated_date: datetime = Field(..., description="Updating date and time of task")
