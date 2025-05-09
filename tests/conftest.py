# import pytest

# from httpx import AsyncClient, ASGITransport
# from typing import AsyncGenerator
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
# from sqlalchemy.pool import NullPool

# from src.db.database import get_async_session, Base
# from src.config import (
#     DB_HOST_TEST,
#     DB_NAME_TEST,
#     DB_PASS_TEST,
#     DB_PORT_TEST,
#     DB_USER_TEST,
# )
# from src.main import app


# DATABASE_URL_TEST = f"postgresql+asyncpg://{DB_USER_TEST}:{DB_PASS_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}"

# engine_test = create_async_engine(DATABASE_URL_TEST, poolclass=NullPool)
# async_session_maker = async_sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)
# Base.metadata.bind = engine_test


# async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session

# app.dependency_overrides[get_async_session] = override_get_async_session


# @pytest.fixture(autouse=True, scope='session')
# async def prepare_database():
#     async with engine_test.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     yield
#     async with engine_test.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)


# @pytest.fixture(scope="session")
# async def ac() -> AsyncGenerator[AsyncClient, None]:
#     transport = ASGITransport(app)
#     async with AsyncClient(transport=transport, base_url="http://test") as ac:
#         yield ac
