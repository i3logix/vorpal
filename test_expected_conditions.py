"""Unit tests for expected conditions functions"""
from unittest import mock
from vorpal import wait_until

def test_condition_called():
    """Test that the condition function is called only once if it immediately returns True"""
    condition = mock.MagicMock(return_value=True)
    wait_until(condition)
    condition.assert_called_once()

def test_condition_called_after_wait():
    """Test that the condition function is called twice if it returns False then True"""
    condition = mock.MagicMock(side_effect=[False, True], polling_frequency_seconds=0.00001)
    wait_until(condition)
    assert condition.call_count == 2
