from typing import Dict

from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def root() -> Dict:
    return dict(status='ok')


@router.get('/version')
async def version() -> Dict:
    return dict(version='1')
