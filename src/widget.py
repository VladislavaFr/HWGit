from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(name_and_number_of_card: str) -> str:
    """Функция маскировки имени и номера/счета банковской карты"""
    string_split = name_and_number_of_card.split(" ")
    numbers = string_split[-1]
    if len(numbers) == 16 or (not numbers.isdigit()):
        return f"{' '.join(string_split[:-1])} {get_mask_card_number(numbers)}"
    elif len(numbers) == 20 or (not numbers.isdigit()):
        return f"{' '.join(string_split[:-1])} {get_mask_account(numbers)}"


def get_date(user_date: str) -> str:
    """Функция которая принимает на вход строку (например:"2024-03-11T02:26:18.671407")
    и выводить:"ДД.ММ.ГГГГ"""
    only_date = user_date[0:10]
    return f"{only_date[8:10]}.{only_date[5:7]}.{only_date[0:4]}"