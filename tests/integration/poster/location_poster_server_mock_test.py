import unittest

from tests.factories import LocationFactory
from tests.integration.poster.location_poster_server_mock import LocationPosterServerMock


class LocationTestPosterServerMock(unittest.TestCase):

    def test_sync_location(self):
        location = LocationFactory.build
