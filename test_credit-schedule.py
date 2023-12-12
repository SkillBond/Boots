import pytest

from credit_schedule import credit_schedule

@pytest.mark.parametrize("amount, percent, time, date, expected", [
    (12000, 5, 6, "01-01-2000", [
        {'date': '31-01-2000', 'overpayment': 500, 'payment': 2000, 'fee': 2500, 'remainder': 10000},
        {'date': '01-03-2000', 'overpayment': 400, 'payment': 2000, 'fee': 2400, 'remainder': 8000},
        {'date': '31-03-2000', 'overpayment': 300, 'payment': 2000, 'fee': 2300, 'remainder': 6000},
        {'date': '30-04-2000', 'overpayment': 200, 'payment': 2000, 'fee': 2200, 'remainder': 4000},
        {'date': '30-05-2000', 'overpayment': 100, 'payment': 2000, 'fee': 2100, 'remainder': 2000},
        {'date': '29-06-2000', 'overpayment': 0, 'payment': 2000, 'fee': 2000, 'remainder': 0}]),
    (250000, 5.5, 24, "01-01-2000", [
        {'date': '31-01-2000', 'overpayment': 3787.88, 'payment': 10416.67, 'fee': 14204.55, 'remainder': 239583.33},
        {'date': '01-03-2000', 'overpayment': 3630.05, 'payment': 10416.67, 'fee': 14046.72, 'remainder': 229166.66},
        {'date': '31-03-2000', 'overpayment': 3472.22, 'payment': 10416.67, 'fee': 13888.89, 'remainder': 218749.99},
        {'date': '30-04-2000', 'overpayment': 3314.39, 'payment': 10416.67, 'fee': 13731.06, 'remainder': 208333.32},
        {'date': '30-05-2000', 'overpayment': 3156.57, 'payment': 10416.67, 'fee': 13573.24, 'remainder': 197916.65},
        {'date': '29-06-2000', 'overpayment': 2998.74, 'payment': 10416.67, 'fee': 13415.41, 'remainder': 187499.98},
        {'date': '29-07-2000', 'overpayment': 2840.91, 'payment': 10416.67, 'fee': 13257.58, 'remainder': 177083.31},
        {'date': '28-08-2000', 'overpayment': 2683.08, 'payment': 10416.67, 'fee': 13099.75, 'remainder': 166666.64},
        {'date': '27-09-2000', 'overpayment': 2525.25, 'payment': 10416.67, 'fee': 12941.92, 'remainder': 156249.97},
        {'date': '27-10-2000', 'overpayment': 2367.42, 'payment': 10416.67, 'fee': 12784.09, 'remainder': 145833.3},
        {'date': '26-11-2000', 'overpayment': 2209.6, 'payment': 10416.67, 'fee': 12626.27, 'remainder': 135416.63},
        {'date': '26-12-2000', 'overpayment': 2051.77, 'payment': 10416.67, 'fee': 12468.44, 'remainder': 124999.96},
        {'date': '25-01-2001', 'overpayment': 1893.94, 'payment': 10416.67, 'fee': 12310.61, 'remainder': 114583.29},
        {'date': '24-02-2001', 'overpayment': 1736.11, 'payment': 10416.67, 'fee': 12152.78, 'remainder': 104166.62},
        {'date': '26-03-2001', 'overpayment': 1578.28, 'payment': 10416.67, 'fee': 11994.95, 'remainder': 93749.95},
        {'date': '25-04-2001', 'overpayment': 1420.45, 'payment': 10416.67, 'fee': 11837.12, 'remainder': 83333.28},
        {'date': '25-05-2001', 'overpayment': 1262.63, 'payment': 10416.67, 'fee': 11679.3, 'remainder': 72916.61},
        {'date': '24-06-2001', 'overpayment': 1104.8, 'payment': 10416.67, 'fee': 11521.47, 'remainder': 62499.94},
        {'date': '24-07-2001', 'overpayment': 946.97, 'payment': 10416.67, 'fee': 11363.64, 'remainder': 52083.27},
        {'date': '23-08-2001', 'overpayment': 789.14, 'payment': 10416.67, 'fee': 11205.81, 'remainder': 41666.6},
        {'date': '22-09-2001', 'overpayment': 631.31, 'payment': 10416.67, 'fee': 11047.98, 'remainder': 31249.93},
        {'date': '22-10-2001', 'overpayment': 473.48, 'payment': 10416.67, 'fee': 10890.15, 'remainder': 20833.26},
        {'date': '21-11-2001', 'overpayment': 315.66, 'payment': 10416.67, 'fee': 10732.33, 'remainder': 10416.59},
        {'date': '21-12-2001', 'overpayment': 157.83, 'payment': 10416.67, 'fee': 10574.5, 'remainder': 0}])
])
def test_0(amount, percent, time, date, expected):
    assert credit_schedule(amount, percent, time, date) == expected

@pytest.mark.parametrize("amount, percent, time, date, expected", [
    (-1, 11, 10, "01-01-2000", "Amount must be greater than zero"),
    ("a", 11, 10, "01-01-2000", "Amount must be a number"),
    ("", 11, 10, "01-01-2000", "Amount must be a number"),
    (True, 11, 10, "01-01-2000", "Amount must be a number"),
    (False, 11, 10, "01-01-2000", "Amount must be a number")
])
def test_1(amount, percent, time, date, expected):
    assert credit_schedule(amount, percent, time, date) == expected

@pytest.mark.parametrize("amount, percent, time, date, expected", [
    (10000, -1, 10, "01-01-2000", "Percent must be greater than zero"),
    (10000, "a", 10, "01-01-2000", "Percent must be a number"),
    (10000, "", 10, "01-01-2000", "Percent must be a number"),
    (10000, True, 10, "01-01-2000", "Percent must be a number"),
    (10000, False, 10, "01-01-2000", "Percent must be a number")
])
def test_2(amount, percent, time, date, expected):
    assert credit_schedule(amount, percent, time, date) == expected

@pytest.mark.parametrize("amount, percent, time, date, expected", [
    (10000, 10, -1, "01-01-2000", "Time must be greater then zero"),
    (10000, 10, "a", "01-01-2000", "Time must be a number"),
    (10000, 10, "", "01-01-2000", "Time must be a number"),
    (10000, 10, True, "01-01-2000", "Time must be a number"),
    (10000, 10, False, "01-01-2000", "Time must be a number")
])
def test_3(amount, percent, time, date, expected):
    assert credit_schedule(amount, percent, time, date) == expected

@pytest.mark.parametrize("amount, percent, time, date, expected", [
    (10000, 10, 10, "01-01-fsesdgdgds", "Invalid date"),
    (10000, 10, 10, "", "Invalid date"),
    (10000, 10, 10, 10, "Invalid date"),
    (10000, 10, 10, -1, "Invalid date"),
    (10000, 10, 10, "a", "Invalid date")
])
def test_3(amount, percent, time, date, expected):
    assert credit_schedule(amount, percent, time, date) == expected

@pytest.mark.parametrize("amount, percent, time, date, expected", [
    (-123, 10, 10, "01-01-fsesdgdgds", "Amount must be greater than zero"),
    (10000, "a", -1, "01-01-2020", "Percent must be a number"),
    (10, 10000, "01-01-2000", 10, "Time must be a number"),
    ("112345", -2, 10, "20-02-2020", "Amount must be a number"),
    ("10000", "10", "10", "a", "Amount must be a number"),
    ("10000", "10", "6", "01-01-2000", "Amount must be a number")
])
def test_3(amount, percent, time, date, expected):
    assert credit_schedule(amount, percent, time, date) == expected
