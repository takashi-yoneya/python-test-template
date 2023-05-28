import typing as t

import pytest
from pytest_mock import MockerFixture

from modules.external_api import get_weather


# parametrizeを使用すると、1つのテスト関数で複数のパラメータのパターンを検証することができる
# 以下の例では、3つのパターンを検証している
@pytest.mark.parametrize(
    ["city_code", "expected"],  # paramで使用する変数名を指定する
    [
        # 上記で指定した順番でパラメータを指定する。id=は省略可能だが、指定するとテストを選択的に実行することができる
        pytest.param(130010, {"title": "東京都 東京 の天気"}, id="success_tokyo"),
        pytest.param(400040, {"title": "福岡県 久留米 の天気"}, id="success_fukushima"),
        pytest.param(
            999999,
            {"error": "The specified city ID is invalid."},
            id="failed_not_found_city_code",
        ),
    ],
)
# paramで指定した変数名を引数に指定すると、テスト関数内で使用できる
# test_{{テスト対象の関数名}} という名前にするとわかりやすいです
def test_get_weather(city_code: int, expected: dict[str, t.Any]) -> None:
    # arrange
    # 前処理が必要な場合は記述するが、fixtureを使用する場合は、fixtureの指定のみでarrangeが完結する場合が多い

    # act
    # テスト対象の関数を実行する
    actual_res = get_weather(city_code=city_code)

    # assert
    # dictを部分的に比較する場合は、>=を使用する
    assert actual_res.items() >= expected.items()


# オフライン環境でテストする場合や、簡単にテストできない場合には、mockを使用すると便利です
# pytest_mockをimportすると、mockerというfixtureが使用できるようになります
def test_get_weather_with_mock(mocker: MockerFixture) -> None:
    # arrange
    class MockResponse:
        def __init__(self, json_data: dict[str, t.Any], status_code: int) -> None:
            self.json_data = json_data
            self.status_code = status_code

        def json(self) -> dict[str, t.Any]:
            return self.json_data

    city_code = 999999
    response_dict = {"title": "mocked title"}
    mock_response = MockResponse(json_data=response_dict, status_code=200)

    # mocker.patchで、任意の関数をmockと置き換えることができます
    # 以下の例では、modules/externalのrequests.getをmock_responseに置き換えています
    m = mocker.patch("modules.external_api.requests.get", return_value=mock_response)

    # act
    actual_res = get_weather(city_code=city_code)

    # assert
    # mockで指定した結果がレスポンスされることを確認
    assert actual_res == response_dict

    # mocker.patchの戻り値のobjectはMagicMockというオブジェクトで、呼び出し回数や引数などを検証することができる
    # 1回呼び出されたか
    m.assert_called_once()

    # 1回呼び出されたか、かつ引数が一致するか
    m.assert_called_once_with(
        f"https://weather.tsukumijima.net/api/forecast/city/{city_code}"
    )
