import pytest

from src.generators import transaction_descriptions


def test_transaction_descriptions_basic():
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Оплата услуг"},
        {"description": "Покупка товара"}
    ]

    gen = transaction_descriptions(transactions)

    assert next(gen) == "Перевод организации"
    assert next(gen) == "Оплата услуг"
    assert next(gen) == "Покупка товара"


def test_transaction_descriptions_empty():
    transactions = []
    gen = transaction_descriptions(transactions)

    assert list(gen) == []


def test_transaction_descriptions_missing_key():
    transactions = [
        {},
        {"description": "Операция"},
        {}
    ]

    gen = transaction_descriptions(transactions)

    assert next(gen) == ""
    assert next(gen) == "Операция"
    assert next(gen) == ""
