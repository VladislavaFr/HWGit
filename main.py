from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date

print("Маска карты:", get_mask_card_number("7000792289606361"))
print("Маска счёта:", get_mask_account("73654108430135874305"))

print("Обработка карты/счета:",
      mask_account_card('Visa Platinum <a href="tel:7000792289606361">7000792289606361</a>'))

print("Дата:", get_date("2024-03-11T02:26:18.671407"))

data = [
    {"id": 1, "state": "EXECUTED", "date": "2024-01-01T10:00:00"},
    {"id": 2, "state": "CANCELED", "date": "2023-01-01T10:00:00"},
    {"id": 3, "state": "EXECUTED", "date": "2022-01-01T10:00:00"},
]

print("Фильтрация EXECUTED:", filter_by_state(data))
print("Сортировка по дате (убыв.):", sort_by_date(data))