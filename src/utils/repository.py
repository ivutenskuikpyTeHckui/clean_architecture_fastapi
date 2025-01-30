from abc import ABC, abstractmethod

from sqlalchemy import insert, select

from src.db.database import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplementedError
    
    @abstractmethod
    async def get_all(self):
        raise NotImplementedError
    
    @abstractmethod
    async def delete_one(self, instance_id: int):
        raise NotImplementedError
    
    @abstractmethod
    async def update_one(self, id: int, data: dict):
        raise NotImplementedError
    

class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict, **kwargs ) -> int:
        async with async_session_maker() as session:
            instance = self.model(**data)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance.id
        
    async def get_all(self):
        async with async_session_maker() as session:
            result = await session.execute(select(self.model))
            return result.scalars().all()
        
    async def delete_one(self, instance_id: int):
        async with async_session_maker() as session:
            instance = await session.get(self.model, instance_id)
            await session.delete(instance)
            await session.commit()

    async def update_one(self, data: dict):
        async with async_session_maker() as session:
            updated_instance = self.model(**data)
            stmt = await session.merge(updated_instance)
            await session.commit()
            return updated_instance.id
