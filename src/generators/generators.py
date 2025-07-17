from typing import Iterator, List, Dict


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Фильтрует список транзакций по заданной валюте.

    Args:
        transactions (List[Dict]): Список транзакций, каждая транзакция — словарь.
        currency (str): Валюта для фильтрации.

    Returns:
        Iterator[Dict]: Итератор по транзакциям с указанной валютой.
    """
    return (tx for tx in transactions if tx.get("currency") == currency)


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генерирует описания транзакций из поля 'description'.

    Args:
        transactions (List[Dict]): Список транзакций.

    Yields:
        str: Описание каждой транзакции, если оно есть.
    """
    for tx in transactions:
        if "description" in tx:
            yield tx["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.

    Args:
        start (int): Начальное значение (включительно).
        stop (int): Конечное значение (исключительно).

    Yields:
        str: Номер карты в формате '0000 0000 0000 XXXX' и т.д.
    """
    for num in range(start, stop):
        card = f"{num:016d}"  # 16-значное число с ведущими нулями
        yield f"{card[:4]} {card[4:8]} {card[8:12]} {card[12:]}"