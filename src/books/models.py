from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
from sqlalchemy.sql import func
import uuid

# default=uuid.uuid4
# This will generate same UUID for all rows


class Book(SQLModel, table=True):
    __tablename__ = "books"
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    langauge: str


created_at: datetime = Field(
    sa_column=Column(pg.TIMESTAMP, server_default=func.now())
)

updated_at: datetime = Field(
    sa_column=Column(pg.TIMESTAMP, server_default=func.now(),
                     onupdate=func.now())
)

# String representation of object
# Useful for debugging/logging


def __repr__(self):
    return f"<Book {self.title}>"
