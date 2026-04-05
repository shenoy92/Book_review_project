from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel
from sqlalchemy.orm import sessionmaker

from src.config import Config

# Connection manager to your database
#  echo=TrueLogs all SQL queries in console
async_engine = create_async_engine(
    url=Config.DATABASE_URL,
    echo=True
)

# async_engine.begin()
# → opens DB connection
# conn.run_sync(...)
# → runs sync code inside async context
# SQLModel.metadata.create_all
# → creates all tables
# What is metadata?
# It stores all models (tables)
# Tables automatically created in DB at startup


async def init_db() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


# What is Session?
# Session = conversation with DB
# You query
# You insert
# You update

# Parameters:
# bind=async_engine
# Connects session to DB engine
#  class_=AsyncSession
# Makes it async
# expire_on_commit=False
# Important setting:
# Normally:
# After commit → objects get cleared
# With this:
# Data stays usable after commit

async def get_session() -> AsyncSession:
    Session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False

    )

    async with Session() as session:
        yield session
