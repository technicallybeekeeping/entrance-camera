"""
Test the IPAddressChecker class
"""

import pytest
from src.IPAddressChecker import IPAddressChecker

# Globals
fake_value = None


class _IPAddressStub:
    def __init__(self, initialValue="10.1.1.1"):
        global fake_value
        fake_value = initialValue

    @staticmethod
    def get():
        global fake_value
        return fake_value


def test_has_changed_once():
    sut = IPAddressChecker(ipaddress=_IPAddressStub())
    result = sut.has_changed()
    assert result is False


def test_has_changed_twice_without_change():
    global fake_value
    sut = IPAddressChecker(ipaddress=_IPAddressStub())
    sut.has_changed()
    result = sut.has_changed()
    assert result is False


def test_has_changed_twice_with_change():
    global fake_value
    sut = IPAddressChecker(ipaddress=_IPAddressStub())
    sut.has_changed()
    fake_value = "20.2.2.2"
    result = sut.has_changed()
    assert result is True


def test_has_changed_three_times_with_one_change():
    global fake_value
    sut = IPAddressChecker(ipaddress=_IPAddressStub())
    sut.has_changed()
    fake_value = "20.2.2.2"
    sut.has_changed()
    result = sut.has_changed()
    assert result is False


def test_has_changed_three_times_with_one_change_last():
    global fake_value
    sut = IPAddressChecker(ipaddress=_IPAddressStub())
    sut.has_changed()
    sut.has_changed()
    fake_value = "20.2.2.2"
    result = sut.has_changed()
    assert result is True
