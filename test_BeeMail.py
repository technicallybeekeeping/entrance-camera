import pytest
from BeeMail import BeeMail

def test_justtest():
    sut = BeeMail()
    result = sut.justTest()
    assert "hello" == result

#def test_sendImage():
#    p1 = BeeMail()
    #p1.sendImage("./photos/hive1.jpg")
