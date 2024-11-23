# conftest.py
import os
import sys

# Add src directory to Python path
src_path = os.path.join(os.path.dirname(__file__), "src")
sys.path.append(src_path)

import logging

# Set up logging
logging.basicConfig(
    filename="pytest.log",
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    filemode="a",
)

logger = logging.getLogger(__name__)

def pytest_runtest_logreport(report):
    if report.failed:
        logger.error(f"Test {report.nodeid} failed:\n{report.longrepr}")
