from cipher_kk3466 import __version__
from cipher_kk3466 import cipher_kk3466

def test_version():
    assert __version__ == '0.1.0'
    
    
def test_cipher():
    expected = 'dpejoh'
    actual = cipher_kk3466.cipher("coding", 1, True)
    assert actual == expected