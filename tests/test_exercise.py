import pytest
import src.exercise

def test_exercise():
    input_values = ["Dave","a mechanic"]
    input_values_stored = ["Dave","a mechanic"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert [output[0],output[1],output[2],output[3],output[4],output[5],output[6]] == ["I will tell you a story, but I need some information first.",\
                                                "What is the main character called?",\
                                                "What is their job?",\
                                                "Here is the story:",\
                                                "Once upon a time there was Dave, who was a mechanic.",\
                                                "On the way to work, Dave reflected on life.",\
                                                "Perhaps Dave will not be a mechanic forever."]
