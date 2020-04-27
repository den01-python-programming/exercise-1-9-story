import pytest
from src.exercise import main

def test_exercise(capsys):
    main()
    output = []
    output,err = capsys.readouterr()

    assert output == "Chicken:\n9000\nBacon (kg):\n0.1\nTractor:\nNone!\n\nAnd finally, a summary:\n9000\n0.1\nNone!\n"
