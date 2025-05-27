import pytest
from opentools1 import Flights
from datetime import date

def test_flights():
    flights_tool = Flights()
    flights = flights_tool.search_flights("JFK", "LAX", date(2025, 6, 15))

    assert len(flights) == 4
