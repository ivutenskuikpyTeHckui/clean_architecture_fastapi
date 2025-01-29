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
    async def delete_one(self, instance_id:int):
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
            print(instance_id)
            instance = await session.get(self.model, instance_id)
            print(instance)
            await session.delete(instance)
            await session.commit()

            