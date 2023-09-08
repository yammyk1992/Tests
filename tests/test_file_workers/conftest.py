import pytest as pt


@pt.fixture(autouse=True)
def clean_text_file():
    with open("prod_file_replica.txt", "w"):
        pass
