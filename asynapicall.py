import httpx
import asyncio


async def fetch_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"


    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        kes_rate = data["rates"]["KES"]
        print(f"1 USD = {kes_rate} KES")
        print(f"100 USD = {100 * kes_rate} KES")

#Run the async function
asyncio.run(fetch_exchange_rate())