import os
from pathlib import Path

data_store_dir_path = os.path.join(
    Path(__file__).parent.parent.absolute(), "data_store"
)


def save_data_store(data_store_name: str, data_text: str) -> int:
    with open(os.path.join(data_store_dir_path, data_store_name), "a") as f:
        return f.write(data_text + "\n")


def get_data_store(data_store_name: str) -> list[str]:
    with open(os.path.join(data_store_dir_path, data_store_name)) as f:
        data_list = f.read()

    return data_list.split("¥n")
