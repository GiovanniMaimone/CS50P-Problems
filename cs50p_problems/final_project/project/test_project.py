import pytest
from unittest.mock import patch
from project import get_food, get_food_info, get_choice


def main():
    test_get_choice()
    test_get_food()
    test_get_food_info()


@pytest.fixture
def mock_data_base():
    return {
        "chicken": {
            "calories": float("100"),
            "serving_size": float("100"),
            "protein": float("10"),
            "carbs": float("10"),
            "fats": float("1"),
        },
        "kfc,chicken": {
            "calories": float("200"),
            "serving_size": float("200"),
            "protein": float("20"),
            "carbs": float("20"),
            "fats": float("2"),
        },
    }


@pytest.fixture
def mock_food_diary():
    return {
        "1": [
            {
                "food": "chicken",
                "quantity": 200,
                "calories": 200.0,
                "protein": 20,
                "carbs": 20,
                "fats": 20,
            },
            {
                "food": "kfc,chicken",
                "quantity": 200,
                "calories": 400.0,
                "protein": 40,
                "carbs": 40,
                "fats": 40,
            },
        ]
    }


def test_get_choice(monkeypatch, mock_data_base, mock_food_diary):
    day = 1
    inputs = iter(["diary", "chicken", "1", "200", "exit", "no", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with patch("project.get_data_base", return_value=mock_data_base):
        with patch("project.save_food_diary"):
            with pytest.raises(SystemExit) as sys:
                get_choice(mock_food_diary, day)

    assert str(sys.value) == "You exited program"
    assert "1" in mock_food_diary
    assert mock_food_diary["1"][0]["food"] == "chicken"
    assert mock_food_diary["1"][0]["quantity"] == 200
    assert mock_food_diary["1"][0]["calories"] == 200
    assert mock_food_diary["1"][0]["protein"] == 20
    assert mock_food_diary["1"][0]["carbs"] == 20
    assert mock_food_diary["1"][0]["fats"] == 20


@patch("project.process.extract")
def test_get_food(mock_fuzzywuzy):
    mock_fuzzywuzy.return_value = [("chicken", 100), ("kfc,chicken", 90)]

    with patch("builtins.input", side_effect=["chicken", "1", "200", "exit"]):
        food_name, food_quantity = get_food()

    assert food_name == "chicken"
    assert food_quantity == 200

    with patch("builtins.input", side_effect=["chicken", "2", "200", "exit"]):
        food_name, food_quantity = get_food()

    assert food_name == "kfc,chicken"
    assert food_quantity == 200


def test_get_food_info(mock_data_base, mock_food_diary):
    food_name = "chicken"
    food_quantity = float(200)
    real_quantity = food_quantity / mock_data_base[food_name]["serving_size"]
    day = 1

    get_food_info(food_name, food_quantity, mock_data_base, mock_food_diary, day)

    assert mock_food_diary[day][0]["food"] == food_name
    assert mock_food_diary[day][0]["quantity"] == food_quantity
    assert (
        mock_food_diary[day][0]["calories"]
        == mock_data_base[food_name]["calories"] * real_quantity
    )
    assert (
        mock_food_diary[day][0]["protein"]
        == mock_data_base[food_name]["protein"] * real_quantity
    )
    assert (
        mock_food_diary[day][0]["carbs"]
        == mock_data_base[food_name]["carbs"] * real_quantity
    )
    assert (
        mock_food_diary[day][0]["fats"]
        == mock_data_base[food_name]["fats"] * real_quantity
    )


if __name__ == "__main__":
    main()
