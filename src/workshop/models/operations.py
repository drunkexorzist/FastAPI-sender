from datetime import date
from pydantic import BaseModel
from decimal import Decimal
from typing import Optional
from enum import Enum


class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class BaseOperation(BaseModel):
    date: date
    kind: OperationKind
    amount: Decimal
    description: Optional[str]

class Operation(BaseOperation):
    id: int

    class Config:
        orm_mode = True
