from src.masks import get_mask_card_number
from src.masks import get_mask_account
from src.widget import get_date
from src.widget import mask_account_card

card_number = "7000792289606361"
masked_card_number = get_mask_card_number(card_number)
print(masked_card_number)

account_number = "73654108430135874305"
masked_account_number = get_mask_account(account_number)
print(masked_account_number)

card1 = "Maestro 1596837868705199"
mask_card1 = mask_account_card(card1)
card2 = "Visa Classic 6831982476737658"
mask_card2 = mask_account_card(card2)

acc1 = "Maestro 1596837868705199"
mask_acc1 = mask_account_card(acc1)
acc2 = "Visa Classic 6831982476737658"
mask_acc2 = mask_account_card(acc2)