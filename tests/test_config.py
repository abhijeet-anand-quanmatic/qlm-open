import os

import pytest
from src.config import Config


@pytest.fixture
def setup_test_env(tmpdir):
    # テスト用の .env ファイルを一時的に作成
    env_file = tmpdir.join(".env")
    env_file.write("""
        DWAVE_API_TOKEN=dwave
        FIXSTARS_API_TOKEN=fixstars
        QUPIT_API_TOKEN=qupit
    """)

    os.environ["ENV_FILE"] = str(env_file)

    yield env_file

    # テスト終了後にクリーンアップ
    env_file.remove()


def test_config(setup_test_env):
    config = Config(_env_file=setup_test_env)  # type: ignore

    assert config.DWAVE_API_TOKEN == "dwave"
    assert config.FIXSTARS_API_TOKEN == "fixstars"
    assert config.QUPIT_API_TOKEN == "qupit"
