from typing import Iterator, List, Dict, Any


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генератор, который поочередно возвращает описания транзакций.

    :param transactions: Список транзакций (каждая — словарь)
    :return: Итератор строк с описаниями операций
    """
    for transaction in transactions:
        yield transaction.get("description", "")
