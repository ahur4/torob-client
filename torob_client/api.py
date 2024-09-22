from typing import Dict, Any

import requests


class Torob:
    """
    A class to interact with the Torob API to fetch product data.

    Methods:
    - suggestion(q: str) -> dict: Fetches product suggestions based on a query string.
    - search(q: str, page: int = 0) -> dict: Fetches paginated product search results.
    - details(prk: str, search_id: int) -> dict: Fetches detailed information for a specific product.
    - special_offers(page: int = 0) -> dict: Fetches special offers with optional pagination.
    - price_chart(prk: str, search_id: int) -> dict: Fetches price chart data for a specific product.
    - similar_product(prk: str, limit: int) -> dict: Fetches similar products based on a product key.
    """

    def __init__(self) -> None:
        self._base_url = "https://api.torob.com/v4/"
        self._suggestion_url = f"{self._base_url}suggestion2/"
        self._search_url = f"{self._base_url}base-product/search/"
        self._details_url = f"{self._base_url}base-product/details/"
        self._special_offers_url = f"{self._base_url}special-offers/"
        self._price_chart_url = f"{self._base_url}base-product/price-chart/"
        self._similar_product_url = f"{self._base_url}base-product/similar-base-product/"

    def suggestion(self, q: str) -> Dict[str, Any]:
        """
        Fetch product suggestions based on the query string.

        Args:
        - q: Query string to search for suggestions.

        Returns:
        - A dictionary containing the suggestion results.
        """
        params = {"q": q}
        return self._send_get(self._suggestion_url, params)

    def search(self, q: str, page: int = 0) -> Dict[str, Any]:
        """
        Fetch paginated product search results.

        Args:
        - q: Query string to search for products.
        - page: Page number for paginated results (default is 0).

        Returns:
        - A dictionary containing the search results.
        """
        params = {"q": q, "page": page}
        result = self._send_get(self._search_url, params)
        return self.__get_search_data_from_url(result)

    def details(self, prk: str, search_id: int) -> Dict[str, Any]:
        """
        Fetch detailed information for a specific product.

        Args:
        - prk: Product key identifier.
        - search_id: Search identifier for the product.

        Returns:
        - A dictionary containing the product details.
        """
        params = {"prk": prk, "search_id": search_id}
        return self._send_get(self._details_url, params)

    def special_offers(self, page: int = 0) -> Dict[str, Any]:
        """
        Fetch special offers with optional pagination.

        Args:
        - page: Page number for paginated results (default is 0).

        Returns:
        - A dictionary containing the special offers.
        """
        params = {"page": page}
        return self._send_get(self._special_offers_url, params)

    def price_chart(self, prk: str, search_id: int) -> Dict[str, Any]:
        """
        Fetch price chart data for a specific product.

        Args:
        - prk: Product key identifier.
        - search_id: Search identifier for the product.

        Returns:
        - A dictionary containing the price chart data.
        """
        params = {"prk": prk, "search_id": search_id}
        return self._send_get(self._price_chart_url, params)

    def similar_product(self, prk: str, limit: int) -> Dict[str, Any]:
        """
        Fetch similar products based on a product key.

        Args:
        - prk: Product key identifier.
        - limit: Maximum number of similar products to retrieve.

        Returns:
        - A dictionary containing the similar products.
        """
        params = {"prk": prk, "limit": limit}
        return self._send_get(self._similar_product_url, params)

    @staticmethod
    def _send_get(url: str, params: Dict[str, Any] = None, timeout: int = 5) -> Dict[str, Any]:
        """
        Send a GET request to the provided URL with optional parameters.

        Args:
        - url: The API endpoint URL.
        - params: Query parameters for the GET request.
        - timeout: Timeout value for the request in seconds (default is 5).

        Returns:
        - A dictionary containing the JSON response.

        Raises:
        - ConnectionError: If the request fails due to a connection issue.
        """
        try:
            response = requests.get(url, params=params, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.ConnectionError:
            raise ConnectionError("Failed to connect to Torob API.")

    def __get_search_data_from_url(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract 'prk' and 'search_id' from product search results.

        Args:
        - data: The dictionary containing search results.

        Returns:
        - The modified search results with 'prk' and 'search_id' added to each item.
        """
        for item in data.get("results", []):
            prk = self.__extract_param(item["more_info_url"], "prk")
            search_id = self.__extract_param(item["more_info_url"], "search_id")
            item["prk"] = prk
            item["search_id"] = search_id
        return data

    @staticmethod
    def __extract_param(url: str, param: str) -> str:
        """
        Extract a parameter value from a URL.

        Args:
        - url: The URL containing the parameters.
        - param: The parameter to extract from the URL.

        Returns:
        - The value of the extracted parameter.
        """
        param_start = url.find(f"{param}=") + len(param) + 1
        param_end = url.find("&", param_start)
        return url[param_start:param_end] if param_end != -1 else url[param_start:]


if __name__ == '__main__':
    instance = Torob()
    data = instance.details("223801ab-2f16-4e27-96bd-83f653dd3e45", 5000)
    print(data)
