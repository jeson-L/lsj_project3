import os
import time

import pytest


@pytest.fixture(scope='session', autouse=True)
def fixtures():
    yield
    # os.system("allure generate ./report/allure_dir -o ./report/html --clean")
