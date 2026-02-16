from typing import TypeVar,Generic,List,Optional,Dict,Any
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
T = TypeVar('T')
class BaseRepository(Generic[T]):
    #Repository for CRUD operations
    def __init__(self,model_class:Type[T],session:Session):
        self.model_class = model_class
        self.session = session
    
    def get_by_id(self, id:int) ->Optional[T]:
        return self.session.query(self.model_class).get(id)

    def get_all(self, limit:Optional[int]=None, offset:int =0)->List[T]:
        query = self.session.query(self.model_class)
        if limit:
            query = query.limit(limit).offset(offset)
        return query.all
    

