
from unittest import mock
from tests.integration.poster.location_poster_server_mock import LocationPosterServerMock

@mock.patch("timeless.location.requests")
class LocationTestPosterServerMock(requests_mock):

    def setUp(self):
        self.mock = LocationPosterServerMock()

    def test_123(self):
        locations = LocationPosterServerMock(
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
        )
