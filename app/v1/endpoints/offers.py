from fastapi import APIRouter
from sqlmodel import Session, select

from app.core.database import engine
from app.core.models.database import Account, Offer

router = APIRouter()


@router.get('/offers/{account_email}')
def get_offers(account_email: str) -> list[Offer]:
    with Session(engine) as session:
        statement = select(Account).where(Account.email == account_email)
        account = session.exec(statement).one()

        statement = select(Offer).where(Offer.state_id == account.state_id)
        offers = session.exec(statement).all()

        return offers
