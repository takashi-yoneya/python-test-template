import glob
import logging
import os

import pytest

from modules.data_store import save_data_store

logger = logging.getLogger(__name__)


@pytest.fixture(autouse=True)
def setup_data_store() -> None:
    # 事前処理が必要な場合は記述する
    logger.info("setup_data_store")

    # yieldを使用すると、一旦処理を呼び出し元に返す
    yield

    # 呼び出し元の処理が完了後に以下が実行されるので、事後処理が必要な場合に記述する
    # 以下では、登録したテストデータを削除している
    logger.info("teardown_data_store")
    for g in glob.glob("**/data_store/test_*"):
        os.remove(g)


@pytest.fixture
def setup_test_data() -> str:
    data_store_name = "test_store.txt"
    save_data_store(data_store_name=data_store_name, data_text="test_data")

    return data_store_name
