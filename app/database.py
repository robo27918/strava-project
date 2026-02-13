from sqlalchemy import create_engine,text
from sqlalchemy.orm import Session
engine = create_engine("sqlite+pysqlite:///:memory:",echo=True)

# creating context manager for Engine
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x,y) VALUES(:x, :y)"),
             [{"x" :1 , "y":1},
              {"x": 34, "y":25},
            ]
        )
    
    conn.commit()# commits it to the table 

with engine.connect() as conn2:
    result = conn2.execute(text("SELECT x,y from some_table"))
    for row in result:
        print(f"x {row.x} {row.y}")
