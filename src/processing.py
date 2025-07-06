from typing import Dict
from typing import List


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Сортирует список словарей, в которых поле 'state' овпадает с переданным значением"""
    result = []
    for item in data:
        if item.get("state") == state:
            result.append(item)
    return result


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    def get_date(item: Dict) -> str:
        return item["date"]

    sorted_data = sorted(data, key=get_date, reverse=reverse)
    return sorted_data