import os

from dotenv import load_dotenv

load_dotenv()


TEST_INTEGER = int(os.getenv('TEST_INTEGER') or '270')

TEST_BOOLEAN = os.getenv(
    "TEST_BOOLEAN", 'False').lower() in ('true', '1', 't')

TEST_STRING = os.getenv('TEST_STRING')

