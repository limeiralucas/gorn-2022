from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class Account(SQLModel, table=True):  # type: ignore[call-arg]
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    state_id: Optional[int] = Field(default=None, foreign_key='state.id')


class Offer(SQLModel, table=True):  # type: ignore[call-arg]
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    state_id: Optional[int] = Field(default=None, foreign_key='state.id')

    state: Optional['State'] = Relationship(back_populates='offers')


class State(SQLModel, table=True):  # type: ignore[call-arg]
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    offers: List['Offer'] = Relationship(back_populates='state')


class Purchase(SQLModel, table=True):  # type: ignore[call-arg]
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[datetime] = Field(
        default_factory=datetime.utcnow,
        nullable=False
    )
    total: float
