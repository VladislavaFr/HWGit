from typing import Iterator, List, Dict, Any


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует транзакции по заданному коду валюты и возвращает итератор.

    :param transactions: Список транзакций (каждая — словарь)
    :param currency_code: Код валюты (например, "USD")
    :return: Итератор с транзакциями, где код валюты соответствует заданному
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction
