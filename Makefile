# .PHONYを使用して、make用のコマンドを定義することができます
# @を先頭に付けたコマンドは、コマンドを非表示で実行できます

# 依存パッケージをインストールします
.PHONY: install
install:
	@echo "Installing dependencies"
	@pip install -r requirements.txt

# pre-commitを実行します
.PHONY: pre-commit
pre-commit:
	@echo "Running pre-commit hooks"
	@pre-commit run --all-files

# テストを実行します
.PHONY: test
test:
	@echo "Running tests"
	@python -m pytest -v
