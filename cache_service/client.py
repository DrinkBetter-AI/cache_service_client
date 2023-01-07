from __future__ import print_function

import json
import logging
from typing import List, Dict

import funcy as funcy
import grpc

from cache_service.compiled_protos import caching_pb2
from cache_service.compiled_protos import caching_pb2_grpc

logger = logging.getLogger(__name__)


class CacheServiceClient:
    def __init__(self, host="localhost", port=50051):
        try:
            options = [('grpc.max_send_message_length', 1024 * 1024 * 1024),  # 1GB
                       ('grpc.max_receive_message_length', 1024 * 1024 * 1024)]  # 1GB
            self.channel = grpc.insecure_channel(f"{host}:{port}", options=options)
            self.stub = caching_pb2_grpc.CachingStub(self.channel)
        except Exception as e:
            logger.error("Failed to initialize CachingClient")
            logger.exception(f"Error connecting to {host}:{port}: {e}")

    # To support with statement
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.channel.close()

    @funcy.log_durations(logger.debug)
    def get_vintage_by_id(self, vintage_id: str) -> Dict:
        """ Get vintage detailed by its id
        - If vintage_id is not found, return empty dict
        """
        vintage_id = caching_pb2.VintageID(vintage_id=vintage_id)
        response = self.stub.get_vintage_by_id(vintage_id)
        serialized_vintage = response.serialized_vintage

        vintage = json.loads(serialized_vintage)
        return vintage

    @funcy.log_durations(logger.debug)
    def get_vintages_by_ids(self, vintage_ids: List[str]) -> List[Dict]:
        """Get vintages detailed by their ids.
        - The output list contains only vintages that are found.
        """
        vintage_ids = caching_pb2.VintageIDs(vintage_ids=vintage_ids)
        response = self.stub.get_vintages_by_ids(vintage_ids)
        vintages = response.serialized_vintages

        vintages = [json.loads(json_vintage) for json_vintage in vintages]
        return vintages

    @funcy.log_durations(logger.debug)
    def get_vintage_title_by_id(self, vintage_id: str) -> str:
        """Get vintage title by its id.
        - If vintage is not found, return empty string
        """
        vintage_id = caching_pb2.VintageID(vintage_id=vintage_id)
        response = self.stub.get_vintage_title_by_id(vintage_id)

        vintage_title = response.vintage_title
        return vintage_title

    @funcy.log_durations(logger.debug)
    def get_vintage_titles_by_ids(self, vintage_ids: List[str]) -> List[str]:
        """ Get vintage titles by their ids.
        - If no title is found for a given vintage id, the corresponding title will be an empty string.
        - The order of the returned titles is the same as the order of the given vintage ids.
        """
        vintage_ids = caching_pb2.VintageIDs(vintage_ids=vintage_ids)
        response = self.stub.get_vintage_titles_by_ids(vintage_ids)

        vintage_titles = response.vintage_titles
        return vintage_titles

    @funcy.log_durations(logger.debug)
    def get_price_by_vintage_id(self, vintage_id: str) -> float:
        """Get price by vintage id.
        - If vintage is not found or the price not exits, return 0.
        """
        vintage_id = caching_pb2.VintageID(vintage_id=vintage_id)
        response = self.stub.get_price_by_vintage_id(vintage_id)

        price = response.price
        return price

    @funcy.log_durations(logger.debug)
    def get_prices_by_vintage_ids(self, vintage_ids: List[str]) -> List[float]:
        """Get prices by vintage ids.
        - If no price is found for a given vintage id, the corresponding price will be 0.
        """
        vintage_ids = caching_pb2.VintageIDs(vintage_ids=vintage_ids)
        response = self.stub.get_prices_by_vintage_ids(vintage_ids)

        prices = response.prices
        return prices

    @funcy.log_durations(logger.debug)
    def get_vintage_ids_by_wine_id(self, wine_id: str) -> List[str]:
        """Get vintage ids by wine id.
        - If no vintage is found for a given wine id, return empty list.
        """
        wine_id = caching_pb2.WineID(wine_id=wine_id)
        response = self.stub.get_vintage_ids_by_wine_id(wine_id)

        vintage_ids = response.vintage_ids
        return vintage_ids

    @funcy.log_durations(logger.debug)
    def get_vintage_ids_by_wine_ids(self, wine_ids: List[str]) -> List[str]:
        """Get vintage ids by wine ids.
        - The output are flattened as a list of vintage ids(integers).
        """
        wine_ids = caching_pb2.WineIDs(wine_ids=wine_ids)
        response = self.stub.get_vintage_ids_by_wine_ids(wine_ids)

        vintage_ids = response.vintage_ids
        return vintage_ids

    @funcy.log_durations(logger.debug)
    def get_wine_id_by_vintage_id(self, vintage_id: str) -> str:
        """Get wine id by vintage id.
        - If vintage is not found, return 0.
        """
        vintage_id = caching_pb2.VintageID(vintage_id=vintage_id)
        response = self.stub.get_wine_id_by_vintage_id(vintage_id)

        wine_id = response.wine_id
        return wine_id

    @funcy.log_durations(logger.debug)
    def get_wine_ids_by_vintage_ids(self, vintage_ids: List[str]) -> List[str]:
        """Get wine ids by theirs vintage ids.
        - The order of the returned wine ids is the same as the order of the given vintage ids.
        - Consider using get_unordered_wine_ids_by_vintage_ids if the order of the returned wine ids is not important.
        """
        vintage_ids = caching_pb2.VintageIDs(vintage_ids=vintage_ids)
        response = self.stub.get_wine_ids_by_vintage_ids(vintage_ids)

        wine_ids = response.wine_ids
        return wine_ids

    @funcy.log_durations(logger.debug)
    def get_unordered_wine_ids_by_vintage_ids(self, vintage_ids: List[str]) -> List[str]:
        """Get wine ids by theirs vintage ids.
        - The order of the returned wine ids is not guaranteed.
        - Consider using get_wine_ids_by_vintage_ids if the order of the returned wine ids is important.
        """
        vintage_ids = caching_pb2.VintageIDs(vintage_ids=vintage_ids)
        response = self.stub.get_unordered_wine_ids_by_vintage_ids(vintage_ids)

        wine_ids = response.wine_ids
        return wine_ids

    @funcy.log_durations(logger.debug)
    def get_best_vintage_id_by_wine_id(self, wine_id: str) -> str:
        """Get the best vintage id by its wine id.
        - If no vintage is found for a given wine id, return 0.
        """
        wine_id = caching_pb2.WineID(wine_id=wine_id)
        response = self.stub.get_best_vintage_id_by_wine_id(wine_id)

        vintage_id = response.vintage_id
        return vintage_id

    @funcy.log_durations(logger.debug)
    def get_best_vintage_ids_by_wine_ids(self, wine_ids: List[str]) -> List[str]:
        """Get the best vintage ids by their wine ids.
        - If no vintage is found for a given wine id, the corresponding vintage id will be 0.
        - The order of the returned vintage ids is the same as the order of the given wine ids.
        - Consider using get_unordered_best_vintage_ids_by_wine_ids if
         the order of the returned vintage ids is not important.
        """
        wine_ids = caching_pb2.WineIDs(wine_ids=wine_ids)
        response = self.stub.get_best_vintage_ids_by_wine_ids(wine_ids)

        vintage_ids = response.vintage_ids
        return vintage_ids

    @funcy.log_durations(logger.debug)
    def get_unordered_best_vintage_ids_by_wine_ids(self, wine_ids: List[str]) -> List[str]:
        """Get the best vintage ids by their wine ids.
        - If no vintage is found for a given wine id, the output does not take into account this wine id.
        - The order of the returned vintage ids is not guaranteed.
        - Consider using get_best_vintage_ids_by_wine_ids if the order of the returned vintage ids is important.
        """
        wine_ids = caching_pb2.WineIDs(wine_ids=wine_ids)
        response = self.stub.get_unordered_best_vintage_ids_by_wine_ids(wine_ids)

        vintage_ids = response.vintage_ids
        return vintage_ids

    @funcy.log_durations(logger.debug)
    def get_high_rated_vintage_ids_from_wine_id(self, wine_id: str) -> List[str]:
        """Get high rated vintage ids from a given wine id.
        - If no vintage is found for a given wine id, return empty list.
        """
        wine_id = caching_pb2.WineID(wine_id=wine_id)
        response = self.stub.get_high_rated_vintage_ids_from_wine_id(wine_id)

        vintage_ids = response.vintage_ids
        return vintage_ids

    @funcy.log_durations(logger.debug)
    def get_high_rated_vintage_ids_from_wine_ids(self, wine_ids: List[str]) -> List[str]:
        """Get high rated vintage ids from a given wine ids.
        - The output are flattened as a list of vintage ids.
        """
        wine_ids = caching_pb2.WineIDs(wine_ids=wine_ids)
        response = self.stub.get_high_rated_vintage_ids_from_wine_ids(wine_ids)

        vintage_ids = response.vintage_ids
        return vintage_ids
