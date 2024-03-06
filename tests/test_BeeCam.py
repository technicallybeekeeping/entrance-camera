#!/usr/bin/env python
"""
Test the BeeCam class
"""

import pytest
from src.BeeCam import BeeCam


class _PiCamera2Stub:
    def start_and_capture_file(self, path, show_preview):
        return True


class _PiCamera2ExceptionThrowerStub:
    def start_and_capture_file(self, path, show_preview):
        raise Exception('Explode!', 'Please!')


def test_start_and_capture_file():
    sut = BeeCam(cam=_PiCamera2Stub())
    result = sut.start_and_capture_file()
    assert result is True


def test_start_and_capture_file_exception():
    sut = BeeCam(cam=_PiCamera2ExceptionThrowerStub())
    result = sut.start_and_capture_file()
    assert result is False

    # with pytest.raises(Exception) as exc_info:   
    #     sut.start_and_capture_file()
    # # these asserts are identical; you can use either one   
    # assert exc_info.value.args[0] == 'some info'
    # assert str(exc_info.value) == 'some info'