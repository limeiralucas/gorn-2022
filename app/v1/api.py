from typing import Dict

from fastapi import APIRouter

from app.v1.endpoints import offers

router = APIRouter(prefix='/v1')
router.include_router(offers.router)


@router.get('/')
async def root() -> Dict:
    return dict(status='ok')


@router.get('/version')
async def version() -> Dict:
    return dict(version='1')
