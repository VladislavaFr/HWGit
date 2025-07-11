from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default():
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
    ]
    result = filter_by_state(data)

    for item in result:
        assert item["state"] == "EXECUTED"


def test_filter_by_state_canceled():
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "CANCELED"},
    ]

    result = filter_by_state(data, state="CANCELED")

    for item in result:
        assert item["state"] == "CANCELED"


def test_sort_by_date_desc():
    data = [
        {"id": 1, "date": "2023-01-01T00:00:00"},
        {"id": 2, "date": "2024-01-01T00:00:00"},
        {"id": 3, "date": "2022-01-01T00:00:00"},
    ]

    sorted_data = sort_by_date(data)
    assert sorted_data[0]["date"] == "2024-01-01T00:00:00"
    assert sorted_data[-1]["date"] == "2022-01-01T00:00:00"


def test_sort_by_date_asc():
    data = [
        {"id": 1, "date": "2023-01-01T00:00:00"},
        {"id": 2, "date": "2024-01-01T00:00:00"},
        {"id": 3, "date": "2022-01-01T00:00:00"},
    ]

    sorted_data = sort_by_date(data, reverse=False)
    assert sorted_data[0]["date"] == "2022-01-01T00:00:00"
    assert sorted_data[-1]["date"] == "2024-01-01T00:00:00"
