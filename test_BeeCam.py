#!/usr/bin/env python
"""
Test the BeeCam class
"""

import pytest
from BeeCam import BeeCam


class PiCamera2Stub:
    def start_and_capture_file(self, path, show_preview):
        return True


def test_start_and_capture_file():
    sut = BeeCam(cam=PiCamera2Stub())
    result = sut.start_and_capture_file()

    assert result is True