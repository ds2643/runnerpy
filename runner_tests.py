import runner

TEST_DIR = 'pytest_examples/'
TEST_FILES = list(map((lambda x: TEST_DIR + x), ['test_some_pass.py', 'test_all_pass.py', 'test_all_fail.py', 'test_empty']))

def test_pytest_result():
    ''' result of capturing the result of running a test in code is a string '''
    test_file = TEST_FILES[0]
    observed_result = runner.pytest_result(test_file)
    assert isinstance(observed_result, str)

def test_find_total():
    ''' successfully parse result of running tests to yield int representation of total tests for mixed result file '''
    test_file = TEST_FILES[0]
    pytest_result = runner.pytest_result(test_file)
    EXPECTED_TOTAL = 2
    observed_total = runner.find_total(pytest_result)
    assert EXPECTED_TOTAL == observed_total

def test_find_passed():
    ''' successfully parse result of running tests to yield int representation of passed tests for mixed result file '''
    test_file = TEST_FILES[0]
    pytest_result = runner.pytest_result(test_file)
    EXPECTED_PASSED = 1
    observed_passed = runner.find_passed(pytest_result)
    assert EXPECTED_PASSED == observed_passed

def test_find_failed():
    ''' successfully parse result of running tests to yield int representation of failed tests for mixed result file '''
    test_file = TEST_FILES[0]
    pytest_result = runner.pytest_result(test_file)
    EXPECTED_FAILED = 1
    observed_failed = runner.find_failed(pytest_result)
    assert EXPECTED_FAILED == observed_failed

def test_find_time():
    ''' successfully parse result of running tests to yield int representation of passed tests for mixed result file '''
    test_file = TEST_FILES[0]
    pytest_result = runner.pytest_result(test_file)
    observed_time = runner.find_time(pytest_result)
    assert isinstance(observed_time, float)

def test_parse_pytest_result_mixed():
    ''' end-to-end test of parsing test result to dict for test file of mixed results '''
    test_file = TEST_FILES[0]
    EXPECTED_PASSED = 1
    EXPECTED_FAILED = 1
    EXPECTED_TOTAL = 2
    actual = runner.parse_pytest_result(test_file)
    actual_passed = actual["passed"]
    actual_failed = actual["failed"]
    actual_total = actual["total"]
    time = actual["time"]
    assert actual_passed == EXPECTED_PASSED and actual_failed == EXPECTED_FAILED and isinstance(time, float) and actual_total == EXPECTED_TOTAL

def test_parse_pytest_result_passing():
    ''' end-to-end test of parsing test result to dict for test file of uniform passing results '''
    test_file = TEST_FILES[1]
    EXPECTED_PASSED = 2
    EXPECTED_FAILED = None
    EXPECTED_TOTAL = 2
    actual = runner.parse_pytest_result(test_file)
    actual_passed = actual["passed"]
    actual_failed = actual["failed"]
    actual_total = actual["total"]
    time = actual["time"]
    assert actual_passed == EXPECTED_PASSED and actual_failed == EXPECTED_FAILED and isinstance(time, float) and actual_total == EXPECTED_TOTAL

def test_parse_pytest_result_failing():
    ''' end-to-end test of parsing test result to dict for test file of uniform failing results '''
    test_file = TEST_FILES[2]
    EXPECTED_PASSED = None
    EXPECTED_FAILED = 2
    EXPECTED_TOTAL = 2
    actual = runner.parse_pytest_result(test_file)
    actual_passed = actual["passed"]
    actual_failed = actual["failed"]
    actual_total = actual["total"]
    time = actual["time"]
    assert actual_passed == EXPECTED_PASSED and actual_failed == EXPECTED_FAILED and isinstance(time, float) and actual_total == EXPECTED_TOTAL

def test_parse_pytest_result_empty():
    ''' end-to-end test of parsing test result to dict for an empty test file '''
    test_file = TEST_FILES[3]
    EXPECTED_PASSED = None
    EXPECTED_FAILED = None
    EXPECTED_TOTAL = None
    actual = runner.parse_pytest_result(test_file)
    actual_passed = actual["passed"]
    actual_failed = actual["failed"]
    actual_total = actual["total"]
    time = actual["time"]
    assert actual_passed == EXPECTED_PASSED and actual_failed == EXPECTED_FAILED and isinstance(time, float) and actual_total == EXPECTED_TOTAL
