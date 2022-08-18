import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Operation(Base):
    __tablename__ = 'operation'

    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.DATE)
    kind = sa.Column(sa.String)
    amount = sa.Column(sa.Numeric(10, 2))
    description = sa.Column(sa.String, nullable=True)