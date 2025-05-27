from dataclasses import dataclass
from datetime import date
from typing import List

@dataclass
class Flight:
    flight_number: str
    airline: str
    departure_airport: str
    arrival_airport: str
    departure_time: str
    arrival_time: str
    price_usd: float


class Flights:
    def __init__(self):
        # Simulated flight database
        self.mock_flights_db = [
            Flight("DL123", "Delta", "JFK", "LAX", "08:00", "11:00", 320.0),
            Flight("AA456", "American Airlines", "JFK", "LAX", "09:00", "12:30", 295.0),
            Flight("UA789", "United", "JFK", "LAX", "13:00", "16:00", 310.0),
            Flight("B6200", "JetBlue", "JFK", "LAX", "15:00", "18:10", 280.0),
        ]

    def search_flights(self, departure_airport_code: str, arrival_airport_code: str, outbound_date: date) -> List[Flight]:
        matching_flights = [
            flight for flight in self.mock_flights_db
            if flight.departure_airport == departure_airport_code
            and flight.arrival_airport == arrival_airport_code
        ]
        print(f"Found {len(matching_flights)} flights on {outbound_date} from {departure_airport_code} to {arrival_airport_code}.")
        return matching_flights
