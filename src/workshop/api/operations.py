from typing import List

from fastapi import APIRouter
from fastapi import Depends

from ..models.operations import Operation, OperationKind
from ..serveces.operations import OperationsService

router = APIRouter(
    prefix='/operations',
)

@router.get('/', response_model=List[Operation])
def get_operations(
    kind: OperationKind,
    service: OperationsService = Depends()
):
    return service.get_list()