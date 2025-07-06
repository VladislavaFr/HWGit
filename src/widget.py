from src.masks import get_mask_account, get_mask_card_number
from datetime import datetime

def mask_account_card(name_and_number_of_card: str) -> str:
    """Функция маскировки имени и номера/счета банковской карты"""
    string_split = name_and_number_of_card.split(" ")
    numbers = string_split[-1]

    if len(numbers) == 16 and numbers.isdigit():
        return f"{' '.join(string_split[:-1])} {get_mask_card_number(numbers)}"
    elif len(numbers) == 20 and numbers.isdigit():
        return f"{' '.join(string_split[:-1])} {get_mask_account(numbers)}"
    else:
        raise ValueError("Номер карты или счета некорректный")


def get_date(user_date: str) -> str:
    """Преобразует дату в из формата ISO в ДД.ММ.ГГГГ"""
    dt = datetime.fromisoformat(user_date)
    return dt.strftime("%d.%m.%Y")