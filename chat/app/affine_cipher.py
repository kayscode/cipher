"""
    this module define an affine cipher algorithm or encrypting message data
"""

class AffineCipher:
    """
        this class provide an interface encrypt and decrypt for ciphering a message
    """

    def __init__(self) -> None:
        self.__letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W'
                          'X','Y','Z']
        
        
    def __is_a_and_b_keys_are_coprime(self,a_key: int, b_key : int) -> bool:
        """
            check if a and be keys of affine cipher are coprime
        """
        
        # check if a_key a other divisor expect himself and one
        a_key_number_list = self.__find_divisor_for_number(a_key)
        b_key_number_list = self.__find_divisor_for_number(b_key)

        if len(a_key_number_list) > 0 or len(b_key_number_list) > 0:
            return False
        else:
            return True


    def __find_divisor_for_number(self, random_number):
        """
             this function find all divisor except 1 and the number itself
        """
        return  [i for i in range (2,(int(random_number/2))+1) if random_number % i == 0]
        

    def encrypt_message(self, a_key:int, b_key:int, message_text: str) -> str:
        """
            encrypt message text by using a and b key
        """
        if self.__is_a_and_b_keys_are_coprime(a_key, b_key):
            encrypted_message = ""

            for letter in message_text.upper():
                encrypted_message += self.__encrypt_message_letter(a_key,b_key,letter)
            
            return encrypted_message
        else:
            return ""
    
    def __encrypt_message_letter(self, a_key: int, b_key: int, message_letter: str):
        """
            this class is responsible to find the encrypted letter for each letter of the
            clear message text
        """
        enrypted_letter_index = (a_key * self.__letters.index(message_letter) + b_key ) % 26
        return self.__letters[enrypted_letter_index]
    

    def __decrypt_message_letter(self,a_key: int, b_key: int, message_letter: str) ->str:
        """
            this function take a encrypted letter with afficne cipher and decrypt it
        """
        decrypt_letter_index = 23 * (message_letter - b_key) % 26
        return self.__letters[decrypt_letter_index]


    def decrypt_message(self, a_key: int, b_key: int , encryted_text: str):
        """
            decrypte a message text by using a and b key
        """

        if self.__is_a_and_b_keys_are_coprime(a_key, b_key):
            orginal_message = ""

            for encrypted_letter in encryted_text:
                orginal_message += self.__decrypt_message_letter(a_key, b_key, encrypted_letter)
            
            return orginal_message
        else:
            return ""