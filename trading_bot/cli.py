import argparse
import sys
from bot.logging_config import setup_logging
from bot.client import BinanceTestnetClient
from bot.orders import execute_futures_order

# Put your real API keys right here inside the quotes
API_KEY = "zeIOlUm3VzjmSkWlKZALUN1v4hvIsrJb9DaIgcDqVkPKKSgzk2lt6BfSB3FKwBZf"
API_SECRET = "ilrOpeGkNwVEt3GnhbujOC1dDokIh3ggDHYkpMroJTjgUkMuP6NrQVBzTLHsY6Ie"

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Simplified Binance Futures Testnet Trading Bot CLI")
    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float, help="Amount to trade")
    parser.add_argument("--price", type=float, help="Price (Required ONLY for LIMIT orders)")

    args = parser.parse_args()

    try:
        bot_client = BinanceTestnetClient(API_KEY, API_SECRET)
        success, result = execute_futures_order(
            client_wrapper=bot_client, symbol=args.symbol, side=args.side, 
            order_type=args.type, quantity=args.quantity, price=args.price
        )

        print("\n" + "="*40)
        if success:
            print("[+] ORDER CONFIRMED")
            for key, val in result.items():
                print(f" > {key}: {val}")
        else:
            print(f"[-] ORDER FAILED\nReason: {result}")
        print("="*40 + "\n")

    except Exception as e:
        print(f"\n[!] Error: {str(e)}\n")

if __name__ == "__main__":
    main()
