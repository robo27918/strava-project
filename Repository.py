from typing import Type, List
from pydantic import BaseModel
import psycopg

class BaseRepository:
    def __init__(self, conn: psycopg.Connection, model: Type[BaseModel], table_name: str):
        self.conn = conn
        self.model = model
        self.table_name = table_name

    def read_all(self) -> List[BaseModel]:
        with self.conn.cursor() as cur:
            cur.execute(f'SELECT * FROM "{self.table_name}"')
            rows = cur.fetchall()
            return [self.model(**dict(zip([desc[0] for desc in cur.description], row))) for row in rows]

    def read_one(self, id: int):
        with self.conn.cursor() as cur:
            cur.execute(f'SELECT * FROM "{self.table_name}" WHERE id = %s', (id,))
            row = cur.fetchone()
            if row:
                return self.model(**dict(zip([desc[0] for desc in cur.description], row)))
            return None

    def insert(self, data: dict):
        obj = self.model(**data)  # validation
        fields = ', '.join(data.keys())
        placeholders = ', '.join(['%s']*len(data))
        values = tuple(data.values())
        with self.conn.cursor() as cur:
            cur.execute(f'INSERT INTO "{self.table_name}" ({fields}) VALUES ({placeholders})', values)
            self.conn.commit()
