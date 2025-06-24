def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскировки номера банковской карты"""
    if len(card_number) != 16 or (not card_number.isdigit()):
        print("Попробуйте снова")
    else:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number):
    """Функция маскировки номера банковского счета"""
    if len(account_number) != 20 or (not account_number.isdigit()):
        print("Попробуйте снова")
    else:
        return f"**{account_number[-4:]}"