import os
import requests
from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv()
API_KEY = os.getenv("CURRENCY_API_KEY")

def convert_to_rubles(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли (RUB).
    Поддерживает USD и EUR. Если валюта RUB, возвращает сумму как есть.

    :param transaction: словарь с ключами 'operationAmount' -> {'amount': float, 'currency': {'code': str}}
    :return: сумма в рублях
    """
    amount = transaction.get("operationAmount", {}).get("amount")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    if currency == "RUB":
        return float(amount)

    if not API_KEY:
        raise ValueError("API ключ не найден. Убедитесь, что CURRENCY_API_KEY задан в .env")

    response = requests.get(
        "https://api.apilayer.com/exchangerates_data/latest",
        params={"base": currency, "symbols": "RUB"},
        headers={"apikey": API_KEY}
    )

    response.raise_for_status()
    data = response.json()
    rate = data["rates"]["RUB"]
    return round(float(amount) * rate, 2)
