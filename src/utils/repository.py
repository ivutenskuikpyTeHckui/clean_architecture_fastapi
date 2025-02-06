from abc import ABC, abstractmethod

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

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

    def __init__(self, session:AsyncSession):
        self.session = session

    async def add_one(self, data: dict, **kwargs ) -> int:
        instance = self.model(**data)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance.id
        
    async def get_all(self):
        result = await self.session.execute(select(self.model))
        return result.scalars().all()
        
    async def delete_one(self, instance_id: int):
        instance = await self.session.get(self.model, instance_id)
        await self.session.delete(instance)
        await self.session.commit()

    async def update_one(self, data: dict):
        updated_instance = self.model(**data)
        stmt = await self.session.merge(updated_instance)
        await self.session.commit()
        return updated_instance.id
