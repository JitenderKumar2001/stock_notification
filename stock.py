
import requests
import time
from plyer import notification

def fetch_stock_price(symbol):
    api_key = "7NITAIZ8XSTV217H"
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    if "Global Quote" in data:
        price = data["Global Quote"]["05. price"]
        return price
    else:
        return None

def send_notification(symbol, price):
    notification_title = f"Stock Price Update: {symbol}"
    notification_message = f"Current Price: {price}"
    notification.notify(
        title=notification_title,
        message=notification_message,
        timeout=10
    )

def main():
    symbol = "AAPL"
    while True:
        price = fetch_stock_price(symbol)
        if price:
            send_notification(symbol, price)
        else:
            print("Error fetching stock price.")
        time.sleep(30)

if __name__ == "__main__":
    main()
