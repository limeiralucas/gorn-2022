from fastapi import APIRouter
from sqlmodel import Session, select

from app.core.database import engine
from app.core.models.database import Account, Offer

router = APIRouter()

DEFAULT_OFFERS = [
    {
        'id': 0,
        'name': 'Decoration',
        'price': 2000.0,
        'state_id': 0
    },
    {
        'id': 0,
        'name': 'Grill',
        'price': 1300.0,
        'state_id': 0
    }
]


@router.get('/offers/{account_email}')
def get_offers(account_email: str) -> list[Offer]:
    with Session(engine) as session:
        statement = select(Account).where(Account.email == account_email)
        account = session.exec(statement).one()

        statement = select(Offer).where(Offer.state_id == account.state_id)
        offers = session.exec(statement).all() or DEFAULT_OFFERS

        return offers
