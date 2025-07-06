from typing import List, Dict


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Возвращает список словарей, в которых поле 'state' совпадает с переданным значением.
    """
    result = []
    for item in data:
        if item.get("state") == state:
            result.append(item)
    return result


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по полю 'date'. По умолчанию — по убыванию (reverse=True).
    """

    def get_date(item: Dict) -> str:
        return item["date"]

    return sorted(data, key=get_date, reverse=reverse)
