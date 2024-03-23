#!/usr/bin/env python
"""
Test the BeeCam class
"""

import pytest
from src.BeePhoto import BeePhoto


class _PiCamera2Stub:
    def start_and_capture_file(self, path, show_preview):
        return True


class _PiCamera2ExceptionThrowerStub:
    def start_and_capture_file(self, path, show_preview):
        raise Exception('Explode!', 'Please!')


class _FileNameFormatterStub:
    def get_file_name(self):
        return "stubbed"


def test_start_and_capture_file():
    sut = BeePhoto(cam=_PiCamera2Stub(), formatter=_FileNameFormatterStub())
    result = sut.capture_photo()
    assert result is True


def test_start_and_capture_file_exception():
    sut = BeePhoto(cam=_PiCamera2ExceptionThrowerStub(),
                   formatter=_FileNameFormatterStub())
    result = sut.capture_photo()
    assert result is False

    # with pytest.raises(Exception) as exc_info:   
    #     sut.start_and_capture_file()
    # # these asserts are identical; you can use either one   
    # assert exc_info.value.args[0] == 'some info'
    # assert str(exc_info.value) == 'some info'