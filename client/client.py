"""
Description: File which contains the Client
class which manages the client data.
"""

__author__ = "Sahil Choudhary"
__version__ = "1.0.0"
__credits__ = "Sahil Choudhary"

from email_validator import validate_email, EmailNotValidError

class Client:
    """
    Client class: Used to store and manage client information.
    """

    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str) -> None:
        """
        Initializes the client attributes.

        Args:
            client_number (int): The unique identifier for the client.
            first_name (str): The client's first name.
            last_name (str): The client's last name.
            email_address (str): The client's email address.

        Returns:
            None

        Raises:
            ValueError: If client_number is not an integer, or first_name or last_name are empty.
            EmailNotValidError: If the email_address is in an invalid format.
        """
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be an integer.")

        if first_name.strip():
            self.__first_name = first_name
        else:
            raise ValueError("First name cannot be empty.")

        if last_name.strip():
            self.__last_name = last_name
        else:
            raise ValueError("Last name cannot be empty.")

        try:
            validated_email = validate_email(email_address)
            self.__email_address = validated_email.normalized
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"

    
    @property
    def client_number(self) -> int:
        """
        Retrieves the client number.

        Args:
            None

        Returns:
            int: The client's unique identification number.
        """
        return self.__client_number

    # Getter for the first_name attribute
    @property
    def first_name(self) -> str:
        """
        Retrieves the first name of the client.

        Args:
            None

        Returns:
            str: The client's first name.
        """
        return self.__first_name

    # Getter for the last_name attribute
    @property
    def last_name(self) -> str:
        """
        Retrieves the last name of the client.

        Args:
            None

        Returns:
            str: The client's last name.
        """
        return self.__last_name

    # Getter for the email_address attribute
    @property
    def email_address(self) -> str:
        """
        Retrieves the email address of the client.

        Args:
            None

        Returns:
            str: The client's email address.
        """
        return self.__email_address
    
def __str__(self) -> str:
    """
    Generates a string representation of the Client instance.

    Args:
        None

    Returns:
        str: A formatted string displaying the client's details.
    """
    return f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_address}\n"


