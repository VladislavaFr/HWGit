
from src.masks import get_mask_account
from src.masks import get_mask_card_number
from src.processing import sort_by_date

print(get_mask_card_number("7000792289606361"))  # 7000 79** **** 6361
print(get_mask_account("73654108430135874305"))  # **4305

operations = [
    {"id": 1, "state": "EXECUTED", "date": "2024-06-01T10:00:00"},
    {"id": 2, "state": "EXECUTED", "date": "2023-03-15T08:00:00"},
    {"id": 3, "state": "CANCELED", "date": "2024-07-06T20:00:00"},
]

print("По убыванию:")
for item in sort_by_date(operations):
    print(item)

print("По возрастанию:")
for item in sort_by_date(operations, reverse=False):
    print(item)

