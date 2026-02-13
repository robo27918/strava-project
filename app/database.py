from sqlalchemy import create_engine,text,MetaData,Table,Column,Integer,String,Float
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os
load_dotenv()
engine = create_engine(os.getenv("DB_URL"))

# creating context manager for Engine
# with engine.connect() as conn:
#     conn.execute(text("CREATE TABLE some_table (x int, y int)"))
#     conn.execute(
#         text("INSERT INTO some_table (x,y) VALUES(:x, :y)"),
#              [{"x" :1 , "y":1},
#               {"x": 34, "y":25},
#               {'x':55, "y":234},
#               {"x":34, "y":-1},
#               {"x":-25,"y":4521}
#             ]
#         )
    
#    conn.commit()# commits it to the table 

# with engine.connect() as conn2:
    # result = conn2.execute(text("SELECT x,y from some_table"))
    # for row in result:
        # print(f"x {row.x} {row.y}")

# stmt = text("SELECT x,y FROM some_table where y> :y ORDER BY x, y")
# with Session(engine) as sess:
#     result = sess.execute(stmt, {"y":6})
#     for x,y in result:
#         print(f"x:{x} y:{y}")

metadata_obj = MetaData()
summary_activity_table = Table(
    "summary_activity",
    metadata_obj,
    Column('id',Integer,primary_key=True),
    Column('achievement_count',Integer),
    Column('average_speed',Float),
    Column('average_watts',Float),
    Column('elapsed_time',Float),
    Column('elev_high',Float),
    Column('elev_low',Float),
    Column('max_speed',Float),
    Column('moving_time',Float),
    Column('total_elevation_gain',Float),
)
print(summary_activity_table.c.keys())