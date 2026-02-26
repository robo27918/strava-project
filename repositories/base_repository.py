from typing import TypeVar,Generic,List,Optional,Dict,Any,Type
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
T = TypeVar('T')
class BaseRepository(Generic[T]):
    #Repository for CRUD operations
    def __init__(self,model_class:Type[T],session:Session):
        self.model_class = model_class
        self.session = session
    
    def get_by_id(self, id:int) ->Optional[T]:
        return self.session.get(self.model_class,id)

    def get_all(self, limit:Optional[int]=None, offset:int =0)->List[T]:
        query = self.session.query(self.model_class)
        if limit is not None:
            query = query.limit(limit).offset(offset)
        return query.all()
    
    def create(self,**kwargs)-> T:
        '''create new record'''
        instance = self.model(**kwargs)
        self.session.add(instance)
        self.session.flush()

    def update(self, id:int, **kwargs)->Optional[T]:
        instance = self.get_by_id(id)
        if instance:
            for key,value in kwargs.items():
                setattr(instance,key,value)
            self.session.flush()
            print("created new object")
        return instance
    
    def delete(self,id:int)->bool:
        instance = self.get_by_id(id)
        if instance:
            self.session.delete(instance)
            self.session.flush()
            print('Deleted an object')
            return True
        return False


