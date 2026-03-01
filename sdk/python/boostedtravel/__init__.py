"""
BoostedTravel — Agent-native flight search & booking SDK.

Cheaper than booking.com. Built for autonomous agents.

Usage:
    from boostedtravel import BoostedTravel

    bt = BoostedTravel(api_key="trav_...")
    flights = bt.search("GDN", "BER", "2026-03-03")
    bt.unlock(flights.offers[0].id)
    bt.book(flights.offers[0].id, passenger={...})
"""

from boostedtravel.client import BoostedTravel
from boostedtravel.models import (
    FlightOffer,
    FlightSearchResult,
    FlightSegment,
    FlightRoute,
    UnlockResult,
    BookingResult,
    Passenger,
    AgentProfile,
)

__version__ = "0.1.0"
__all__ = [
    "BoostedTravel",
    "FlightOffer",
    "FlightSearchResult",
    "FlightSegment",
    "FlightRoute",
    "UnlockResult",
    "BookingResult",
    "Passenger",
    "AgentProfile",
]
