from os import getenv
from dotenv import load_dotenv
from string import Template
import requests as rq
from flask import abort

load_dotenv()
API_KEY = getenv("NAPI_KEY")
t_url = Template("https://api.nasa.gov/planetary/apod?api_key=$API_KEY&date=$DATE")


def get_and_give_response(date: str) -> dict | None:
    url = t_url.substitute(API_KEY=API_KEY, DATE=date)
    n_response: dict = rq.get(url).json()
    if n_response.get("url") and n_response.get("title"):
        return {
            "url": n_response.get("url"),
            "title": n_response.get("title")
        }
    return abort(400)
