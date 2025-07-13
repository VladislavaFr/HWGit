def filter_by_currency(transactions: list[dict], currency_code: str):
    """
    Генератор, который возвращает транзакции только с указанной валютой.

    :param transactions: список словарей с транзакциями
    :param currency_code: код валюты, например 'USD'
    :yield: транзакции, где валюта соответствует currency_code
    """
    for tx in transactions:
        if tx.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield tx
