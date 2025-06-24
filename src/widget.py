def mask_account_card(name_and_number_of_card: str) -> str | None:
    """Функция маскировки имени и номера/счета банковской карты"""
    string_split = name_and_number_of_card.split(" ")
    numbers = string_split[-1]
    if len(numbers) == 16 or (not numbers.isdigit()):
        print(f"{' '.join(string_split[:-1])} {numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}")
    elif len(numbers) == 20 or (not numbers.isdigit()):
        print(f"{' '.join(string_split[:-1])} **{numbers[-4:]}")



def get_date(user_date):
    """Функция которая принимает на вход строку (например:"2024-03-11T02:26:18.671407")
    и выводить:"ДД.ММ.ГГГГ"""
    only_date = user_date[0:10]
    print(f"{only_date[8:10]}.{only_date[5:7]}.{only_date[0:4]}")
