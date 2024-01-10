from fastapi import FastAPI
# start up server by running the following command:  python3 -m uvicorn main:app --reload
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

conn = psycopg2.connect(dbname=os.environ.get("database"),
                        user=os.environ.get("user"),
                        password=os.environ.get("password"),
                        host=os.environ.get("DBHOST"),
                        port=os.environ.get("db_port"))

@app.get("/")
def read_root():
    return 'Receiving and sending!'

#leaders
@app.get("/leaders")
async def read_leads():
        cur = conn.cursor()
        try:
             cur.execute(
				""" SELECT * FROM leaders;"""
        )

        except Exception as error:
            conn.commit()
            cur.close()
            return "Internal server error", 500

        l = cur.fetchall()
        conn.commit()
        cur.close()

        return l, 200

#tipstricks
@app.get("/tipstricks")
def tips_tricks():
    return 'Tips and tricks route'
#resources
@app.get("/resources")
def read_recs():
    return 'Resources Route'
#kideos
@app.get("/kideos")
def read_kideos():
    return 'Kid videos route'
#careVids
@app.get("/careVids")
def read_cares():
    return 'Caregiver videos route'
#loader.io route
@app.get("/f{process.env.loader}")
def read_loader():
    return {"message": "Hello, FastAPI!"}

#usage - LEAVE BLANKS FOR NOW
# async def get_tipstricks():
#     try:
#         tipstricks = await tipstricks_collection.find({}).to_list(None)
#         return tipstricks
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))