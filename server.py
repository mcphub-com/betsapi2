import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/b365api-b365api-default/api/betsapi2'

mcp = FastMCP('betsapi2')

@mcp.tool()
def bet365_inplay_filter(sport_id: Annotated[Union[int, float, None], Field(description='Default: 1')] = None,
                         league_id: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                         skip_esports: Annotated[Union[bool, None], Field(description='')] = None) -> dict: 
    '''bet365 inplay filter'''
    url = 'https://betsapi2.p.rapidapi.com/v1/bet365/inplay_filter'
    headers = {'x-rapidapi-host': 'betsapi2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'sport_id': sport_id,
        'league_id': league_id,
        'skip_esports': skip_esports,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def bet365_inplay() -> dict: 
    '''bet365 inplay data'''
    url = 'https://betsapi2.p.rapidapi.com/v1/bet365/inplay'
    headers = {'x-rapidapi-host': 'betsapi2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def bet365_inplay_event(FI: Annotated[str, Field(description='')],
                        stats: Annotated[Literal['1', '0', None], Field(description='')] = None,
                        lineup: Annotated[Literal['1', '0', None], Field(description='')] = None) -> dict: 
    '''inplay event with all scores/stats/markets'''
    url = 'https://betsapi2.p.rapidapi.com/v1/bet365/event'
    headers = {'x-rapidapi-host': 'betsapi2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'FI': FI,
        'stats': stats,
        'lineup': lineup,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def bet365_upcoming_events(sport_id: Annotated[Union[int, float], Field(description='Default: 0')],
                           league_id: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                           day: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                           page: Annotated[Union[int, float, None], Field(description='Default: 0')] = None) -> dict: 
    '''get bet365 fixtures'''
    url = 'https://betsapi2.p.rapidapi.com/v1/bet365/upcoming'
    headers = {'x-rapidapi-host': 'betsapi2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'sport_id': sport_id,
        'league_id': league_id,
        'day': day,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def bet365_prematch_odds(FI: Annotated[Union[int, float], Field(description='Default: 0')]) -> dict: 
    '''prematch odds'''
    url = 'https://betsapi2.p.rapidapi.com/v3/bet365/prematch'
    headers = {'x-rapidapi-host': 'betsapi2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'FI': FI,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def bet365_result(event_id: Annotated[Union[int, float], Field(description='Default: 0')]) -> dict: 
    '''to view bet365 event result'''
    url = 'https://betsapi2.p.rapidapi.com/v1/bet365/result'
    headers = {'x-rapidapi-host': 'betsapi2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'event_id': event_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
