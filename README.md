runnerpy
======
small module that allows for interfacing with PyTest results as native Python data struture

Motivation
------
PyTest provides arguably competitive functionality to the built-in UnitTest testing framework. However, the library suffers from one small drawback: Pytest does not provide support for the results of its tests being represented as a native data structure. Instead, running PyTest simply directs a stream of text detailing results to standard out, to be read by the tester.

Under most circumstances, this shortcoming is tolerable. However, this design choice yields inflexibility takes automated analysis of test results difficult. For instance, one might need compare the results of running test under different circumstances. Did more tests fail the first time the tests were run than the second? Which test run took more time? Such information is only accessible through manually reading the results.

runnerpy is a small python module that addresses this shortcoming by catching the results of running PyTest on a specified test file and returning those results as a python dictionary.

Use
------
This simple module can be run called from within a python script:
```python
   import runnerpy as r
    ...
    result = r.parse_pytest_result('test.py')
    print(result)
    # {passed: 8, failed: 2, total: 10, time = 0.02}
```

Approach
------
The result of running the tests is intercepted from std.out, and stored as a string. The resultant string is parsed with regular expressions. Counts of tests passed, tests failed, total tests, and time elapsed during are stored in a dictionary use by the caller.

Tests
------
Tests are written in PyTest and may be run as follows:
`
    $> pytest test.py # from inside runnerpy/ directory
    # ... [result] ...
`
