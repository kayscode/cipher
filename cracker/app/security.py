"""
    this module possess security policy
"""


class SecurityPolice:
    """
        this class define the policy security for password
    """

    def __init__(self, first_name: str, last_name: str, password: str):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.errors = []

    def is_password_respect_policy(self) -> bool:
        """
            test if the password respect the following policy 4 characters 2 letter
            (which are the combination of the first characters of user first_name and
            the first character of user last_name) and 2 number.

        :param password:
        :return:
        """
        if self.__is_password_as_required_length():
            self.__is_two_first_characters_are_letter()
            self.__is_two_last_character_are_integer()
            self.__is_two_first_characters_respect_policy()
            self.__is_two_last_characters_respect_password_policy()

        if len(self.errors):
            return False
        else:
            return True

    def __is_two_last_character_are_integer(self):
        """
            check if character password respect the policy
        :return:
        """
        if self.password[2].isnumeric() and self.password[3].isnumeric():
            return True
        else:
            return False

    def __is_two_first_characters_are_letter(self):
        """
            check if two first password character respect the policy
        :return:
        """
        if self.password[0].isalpha() and self.password[1].isalpha():
            return True
        else:
            return False

    def __is_two_first_characters_respect_policy(self):
        """
            test if the two first characters match the first_name first character and
            the last_Name first character

        :return:
        """
        if self.password[0] != self.first_name[0]:
            self.errors.append("the first password character doesn't respect policy")
            return False

        if self.password[1] != self.last_name[0]:
            self.errors.append("the second password character doesn't respect policy")
            return False

        return True

    def __is_two_last_characters_respect_password_policy(self):
        """
            check if the two last character of the password are number
        :return:
        """
        try:
            if int(self.password[2]) not in range(1, 9):
                self.errors.append("the third password character doesn't respect the policy")
                return False

            if int(self.password[3]) not in range(1, 9):
                self.errors.append("the fourth password character doesn't respect the policy")
                return False
        except ValueError:
            self.errors.append("the third or the fourth password must be number")

        return True

    def __is_password_as_required_length(self):
        if len(self.password) == 4:
            return True
        else:
            self.errors.append("password length must be 4")
            return False

    def get_errors(self):
        return self.errors

    def __str__(self):
        return f"SecurityPolicy({self.first_name},{self.last_name},{self.password})"
