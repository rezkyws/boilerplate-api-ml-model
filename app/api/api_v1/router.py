# api core module for all endpoints
from fastapi import APIRouter
from .endpoints.endpoint_name import ClassName
from .schemas.doc import Doc

router = APIRouter(
    prefix='/api/v1',
    responses = {
        404: {'description': 'Not Found'}
    }
)

@router.post('/endpoint-name')
async def func_name(doc: Doc):
    class_name = ClassName(doc.text)
    result = class_name.get_inference()

    return result