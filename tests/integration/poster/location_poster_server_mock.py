
from http.server import HTTPStatus
from tests.integration.poster.poster_server_mock import PosterServerMock

class LocationPosterServerMock(PosterServerMock):

    def poster(self):
        port = free_port()
        server = PosterServerMock
        server.start(server)
