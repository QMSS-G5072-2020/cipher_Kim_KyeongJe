from cipher_kk3466 import __version__
from cipher_kk3466 import cipher_kk3466

def test_version():
    assert __version__ == '0.1.0'
    
    
def test_cipher():
    example = 'cats'
    shift = 1
    return cipher(example, shift)
    
test_cipher()