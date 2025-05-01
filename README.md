# poc-template

PoCプロジェクトのテンプレートリポジトリ


## Installation

```bash
pdm install
```

## Run Notebooks

```bash
jupyter notebook
```

## Scripts

- lint

    ```bash
    pdm run lint
    ```

- format

    ```bash
    pdm run format
    ```

- test

    ```bash
    pdm run test
    ```

- check (lint, format, and test)

    ```
    pdm run check
    ```

## リポジトリ構成

```
.
├── data                      入出力データ類
├── docs                      ドキュメント類
├── notebooks                 Jupyter Notebook
├── src                       ソースコード一式
└── tests                     テストコード

```
