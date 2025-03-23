# Async API Call

This project demonstrates how to make asynchronous API calls using Python's `httpx` library. Asynchronous programming allows multiple requests to be processed concurrently, improving efficiency and performance.

## Features
- Uses `httpx` for async HTTP requests
- Fetches data from a sample API endpoint
- Implements Python `asyncio` for concurrency

## Requirements
Ensure you have Python installed (version 3.7+ recommended). Install dependencies:

```sh
pip install httpx asyncio
```

## Usage
Run the script using:

```sh
python asynapicall.py
```

## Example Code
```python
import httpx
import asyncio

async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

async def main():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    data = await fetch_data(url)
    print(data)

if __name__ == "__main__":
    asyncio.run(main())
```

## Contributing
Feel free to fork this repository, submit issues, or suggest improvements.

## License
This project is open-source and available under the MIT License.

