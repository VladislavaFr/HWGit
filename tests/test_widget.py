import pytest
from src.widget import mask_account_card, get_date


# Фикстура с примерами строк с картами и счетами
@pytest.fixture
def sample_data():
    return [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ]


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ]
)
def test_mask_account_card(input_str, expected):
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2020-01-01T00:00:00", "01.01.2020"),
    ]
)
def test_get_date(input_date, expected):
    assert get_date(input_date) == expected


def test_mask_account_card_invalid():
    with pytest.raises(ValueError):
        mask_account_card("Неверные данные")
