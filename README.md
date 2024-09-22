
# TOROB Client

![PyPI](https://img.shields.io/pypi/v/torob-client)
![Daily Downloads](https://img.shields.io/pypi/dd/torob-client)
![Monthly Downloads](https://img.shields.io/pypi/dm/torob-client)
[![Telegram-Channel](https://img.shields.io/badge/Telegram--Channel-Ahura_Rahmani-blue)](https://t.me/Ahur4_Rahmani)


A Python client for interacting with the Torob API to fetch products data.
Here's a sample README for your Torob API client:

---

# Torob API Client

A Python client for interacting with the Torob API to fetch product data efficiently and easily.

## Features

- Fetch product suggestions
- Search for products with pagination
- Retrieve detailed information about specific products
- Access special offers
- Get price chart data for products
- Find similar products based on product keys

## Installation

To install the required dependencies, you can use pip:

```bash
pip install torob-client
```

## Usage

To use the Torob API Client, first, create an instance of the `Torob` class, and then call the desired method. Here’s a quick example:

```python
from torob_client import Torob

# Create an instance of the Torob client
client = Torob()

# Fetch product details
data = client.details("223801ab-2f16-4e27-96bd-83f653dd3e45", 5000)
print(data)
```

## Available Methods

### 1. `suggestion(q: str) -> dict`

Fetch product suggestions based on a query string.

**Parameters:**
- `q`: The query string to search for suggestions.

**Returns:**
- A dictionary containing the suggestion results.

### 2. `search(q: str, page: int = 0) -> dict`

Fetch paginated product search results.

**Parameters:**
- `q`: The query string to search for products.
- `page`: Page number for paginated results (default is 0).

**Returns:**
- A dictionary containing the search results.

### 3. `details(prk: str, search_id: int) -> dict`

Fetch detailed information for a specific product.

**Parameters:**
- `prk`: Product key identifier.
- `search_id`: Search identifier for the product.

**Returns:**
- A dictionary containing the product details.

### 4. `special_offers(page: int = 0) -> dict`

Fetch special offers with optional pagination.

**Parameters:**
- `page`: Page number for paginated results (default is 0).

**Returns:**
- A dictionary containing the special offers.

### 5. `price_chart(prk: str, search_id: int) -> dict`

Fetch price chart data for a specific product.

**Parameters:**
- `prk`: Product key identifier.
- `search_id`: Search identifier for the product.

**Returns:**
- A dictionary containing the price chart data.

### 6. `similar_product(prk: str, limit: int) -> dict`

Fetch similar products based on a product key.

**Parameters:**
- `prk`: Product key identifier.
- `limit`: Maximum number of similar products to retrieve.

**Returns:**
- A dictionary containing the similar products.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Your contributions are welcome!

---
