from fastapi import FastAPI, HTTPException, Response
# start up server by running the following command:  python3 -m uvicorn main:app --reload
from helpers import leader_format, tip_format
import psycopg2
from dotenv import load_dotenv
import os
import httpx

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

        return leader_format(l)

#tipstricks / table name is tips_tricks
@app.get("/tipstricks")
def tips_tricks():
    cur = conn.cursor()
    try:
         cur.execute(
				""" SELECT * FROM tips_tricks;"""
        )

    except Exception as error:
        conn.commit()
        cur.close()
        return "Internal server error", 500

    tt = cur.fetchall()
    conn.commit()
    cur.close()

    return tip_format(tt)

#resources
@app.get("/resources")
def read_recs():
    cur = conn.cursor()
    try:
        cur.execute(
				""" SELECT * FROM resources;"""
        )

    except Exception as error:
        conn.commit()
        cur.close()
        return "Internal server error", 500

    rec = cur.fetchall()
    conn.commit()
    cur.close()

    return rec, 200

#kideos
@app.get("/kideos")
async def kid_vids():
    params = {
      'q': 'ms. rachel',
      'part': 'snippet',
      'maxResults': '17',
      'key': os.environ.get("YT_KEY")
    }
    url = f"https://www.googleapis.com/youtube/v3/search"
    async with httpx.AsyncClient() as client:
        # Make the API request
        response = await client.get(url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse and return the video information
            video_info = response.json()
            return video_info
        else:
            # Raise an HTTPException with the error details
            raise HTTPException(status_code=response.status_code, detail=response.text)


#careVids
@app.get("/careVids")
async def care_vids():
    params = {
      'q': 'ABA for parents',
      'part': 'snippet',
      'maxResults': '17',
      'key': os.environ.get("YT_KEY")
    }
    url = f"https://www.googleapis.com/youtube/v3/search"
    async with httpx.AsyncClient() as client:
        # Make the API request
        response = await client.get(url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse and return the video information
            video_info = response.json()
            return video_info
        else:
            # Raise an HTTPException with the error details
            raise HTTPException(status_code=response.status_code, detail=response.text)


#loader.io route
@app.get("/f{process.env.loader}")
def read_loader():
    return {"message": "Hello, FastAPI!"}

#usage - LEAVE BLANKS FOR NOW