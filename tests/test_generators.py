import pytest
from src.generators.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "currency": "USD", "description": "Payment 1"},
        {"id": 2, "currency": "EUR", "description": "Payment 2"},
        {"id": 3, "currency": "USD", "description": "Payment 3"},
    ]


def test_filter_by_currency(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 2
    for tx in result:
        assert tx["currency"] == "USD"


def test_transaction_descriptions(sample_transactions):
    result = list(transaction_descriptions(sample_transactions))
    assert result == ["Payment 1", "Payment 2", "Payment 3"]


def test_card_number_generator():
    start = 1
    stop = 4
    result = list(card_number_generator(start, stop))
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]
    assert result == expected


@pytest.fixture
def sample_transactions():
    return [
        {"currency": "USD", "description": "Payment"},
        {"currency": "EUR", "description": "Transfer"},
        {"currency": "USD", "description": "Refund"},
    ]


@pytest.mark.parametrize("transactions, currency, expected", [
    (
            [{"currency": "USD"}, {"currency": "EUR"}],
            "USD",
            [{"currency": "USD"}]
    ),
    (
            [{"currency": "EUR"}, {"currency": "EUR"}],
            "USD",
            []
    ),
])
def test_filter_by_currency(transactions, currency, expected):
    result = list(filter_by_currency(transactions, currency))
    assert result == expected


def test_transaction_descriptions(sample_transactions):
    result = list(transaction_descriptions(sample_transactions))
    assert result == ["Payment", "Transfer", "Refund"]
