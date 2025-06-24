from src.masks import get_mask_card_number
from src.masks import get_mask_account

card_number = "7000792289606361"
masked_card_number = get_mask_card_number(card_number)
print(masked_card_number)

account_number = "73654108430135874305"
masked_account_number = get_mask_account(account_number)
print(masked_account_number)