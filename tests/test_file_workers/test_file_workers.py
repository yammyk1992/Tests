from my_test_func.file_workers import read_from_file


def create_test_data(test_data):
    with open("prod_file_replica.txt", "a") as f:
        f.writelines(test_data)


def test_read_from_file():
    test_data = ['one\n', 'two\n', 'three\n']
    create_test_data(test_data)
    assert test_data == read_from_file("prod_file_replica.txt")


def test_read_from_file2():
    test_data = ['one\n', 'two\n', 'three\n', 'four\n']
    create_test_data(test_data)
    assert test_data == read_from_file("prod_file_replica.txt")
