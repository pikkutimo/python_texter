from texter import check_for_diffences, calculate_x_position, calculate_wpm

def test_check_for_diffences() -> None:
    assert 0 == check_for_diffences("", "")

def test_check_difference_with_separate_strings() -> None:
    assert 1 == check_for_diffences("test", "pest")

def test_calculate_x_position_columns_10() -> None:
    assert 1 == calculate_x_position(10, "testtest")

def test_calculate_x_position_columns_20() -> None:
    assert 6 == calculate_x_position(20, "testtest")

def test_calculate_wpm_without_errors() -> None:
    test_sentence = 15 * "test"
    assert 12 == calculate_wpm(10, 70, test_sentence, 0)

def test_calculate_wpm_with_10_errors() -> None:
    test_sentence = 15 * "test"
    assert 2 == calculate_wpm(10, 70, test_sentence, 10)