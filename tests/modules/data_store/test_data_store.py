import pytest

from modules.data_store import get_data_store, save_data_store


@pytest.mark.parametrize(
    ["data_store_name", "data_text"],  # paramで使用する変数名を指定する
    [
        # 上記で指定した順番でパラメータを指定する。id=は省略可能だが、指定するとテストを選択的に実行することができる
        pytest.param("test_store.txt", "test_data", id="success"),
    ],
)
def test_save_data_store(data_store_name: str, data_text: str) -> None:
    # arrange
    # 前処理が必要な場合は記述するが、fixtureを使用する場合は、fixtureの指定のみでarrangeが完結する場合が多い

    # act
    # テスト対象の関数を実行する
    actual_res = save_data_store(data_store_name=data_store_name, data_text=data_text)

    # assert
    assert actual_res == len(data_text) + 1


@pytest.mark.parametrize(
    ["data_store_name", "expected_row_count"],  # paramで使用する変数名を指定する
    [
        # 上記で指定した順番でパラメータを指定する。id=は省略可能だが、指定するとテストを選択的に実行することができる
        pytest.param("test_store.txt", 1, id="success"),
    ],
)
# テスト関数で使用したいfixtureを引数に指定する。
# 以下では、setup_test_dataを使用してテストデータを投入している
def test_get_data_store(
    data_store_name: str,
    expected_row_count: int,
    setup_test_data: None,
) -> None:
    # arrange
    # 前処理が必要な場合は記述するが、fixtureを使用する場合は、fixtureの指定のみでarrangeが完結する場合が多い

    # act
    # テスト対象の関数を実行する
    actual_res = get_data_store(data_store_name=data_store_name)

    # assert
    assert len(actual_res) == expected_row_count


def test_get_data_store_raise_data_store_not_found(
    setup_test_data: None,
) -> None:
    # arrange
    # 前処理が必要な場合は記述するが、fixtureを使用する場合は、fixtureの指定のみでarrangeが完結する場合が多い
    data_store_name = "test_not_found.txt"

    # act
    # Exceptionが発生する場合の検証は、pytest.raisesを使用する
    with pytest.raises(FileNotFoundError):
        get_data_store(data_store_name=data_store_name)
