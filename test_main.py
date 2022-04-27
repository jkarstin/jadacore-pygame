import main


def test_main():
    assert main.main(['test_main.py'], 1) == main.EXIT_SUCCESS
