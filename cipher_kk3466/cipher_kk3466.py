def cipher(text, shift, encrypt=True):
    """
    Describe the funtion 
    Encrypt and decrypt a string using the function by different shift number.
    
    Parameters 
    ----------
    text : string
          The string that contains alphabet we would like to encrypt or decrypt.
    
    shift : int
          The int that either positive or negative number to shift text to encrypt or decrypt.
           
    encrypt : bool
          The bool decides the text whether encrypt or not.
          
    
    Returns
    ----------
    str
        The text after it is encrypted or decrypted.
    
    
    Example
    ----------
    >>> from cipher_kk3466 import cipher_kk3466
    >>> text = 'coding'
    >>> shift = 1
    >>> cipher_kk3466.cipher(text, shift, encrypt = True)
    'dpejoh'
    
    """



    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text