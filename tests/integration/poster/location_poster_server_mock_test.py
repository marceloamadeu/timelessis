
import unittest
from tests.integration.poster.location_poster_server_mock import LocationPosterServerMock


class LocationTestPosterServerMock(unittest.TestCase):

    locations = [
        {
            "id":40,
            "name":"Pao Pao Cafe",
            "code":"P",
            "company_id":50,
            "country":"United States",
            "region":"Nay",
            "city":"South",
            "address":"Delta Park, 145",
            "longitude":640,
            "latitude":480,
            "type":"L",
            "status":"open",
            "comment":"Brazilian cafe"
        },
        {
            "id":150,
            "name":"Central Perk",
            "code":"C",
            "company_id":50,
            "country":"United States",
            "region":"Manhattan",
            "city":"New York",
            "address":"5th Avenue 145",
            "longitude":1024,
            "latitude":720,
            "type":"C",
            "status":"open",
            "comment":"Cafe from famous sitcom"
        }
    ]

    """
    def test_sync_location(self):
    """
