Pytestを使用したテストテンプレート
====

# 構成
python: 3.10+
pytest: 7.3+

# 機能

pytest,conftest.py,fixture,pytest-mockを使用したテストテンプレートを実装しています。

# 使い方

makeコマンドを使用していますが、makeコマンドが使用できない環境の場合はMakefike内を参照して、直接コマンドを確認して実行してください。

依存パッケージのインストール

```bash
make install
```

全てのテストケースを実行

```bash
make test
```
