# root conftest
# テスト全体で有効なため、全体共通のfixture等を定義するために使用します

import logging
import os
import sys
from pathlib import Path

import pytest

src_path = os.path.join(Path(__file__).parent.parent.absolute(), "src")
sys.path.append(src_path)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

logger.info("start: root conftest")


@pytest.fixture(autouse=True)
def setup_root() -> None:
    logger.info("start setup_root: テスト全体で使用する前処理を記述")
    yield
    logger.info("end: teardown_root: テスト全体で使用する後処理を記述")


logger.info("end: root conftest")
