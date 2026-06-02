import logging

def execute_futures_order(client_wrapper, symbol, side, order_type, quantity, price=None):
    client = client_wrapper.get_raw_client()
    symbol = symbol.upper()
    side = side.upper()
    order_type = order_type.upper()

    if side not in ['BUY', 'SELL']:
        raise ValueError(f"Invalid side: {side}. Must be BUY or SELL.")
    if order_type not in ['MARKET', 'LIMIT']:
        raise ValueError(f"Invalid order type: {order_type}. Must be MARKET or LIMIT.")
    if order_type == 'LIMIT' and not price:
        raise ValueError("A price is required for LIMIT orders!")

    logging.info(f"[REQUEST SUMMARY] Placing {side} {order_type} order for {quantity} {symbol}...")

    try:
        order_params = {
            'symbol': symbol,
            'side': side,
            'type': order_type,
            'quantity': float(quantity)
        }

        if order_type == 'LIMIT':
            order_params['price'] = str(price)
            order_params['timeInForce'] = 'GTC'

        response = client.futures_create_order(**order_params)

        logging.info("[SUCCESS] Order executed successfully by testnet server.")

        summary = {
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice", "N/A")
        }
        return True, summary

    except Exception as e:
        error_msg = f"[FAILURE] Binance API rejected the order. Reason: {str(e)}"
        logging.error(error_msg)
        return False, str(e)
