__author__ = "Sahil Choudhary"
__version__ = "1.0.0"

from datetime import datetime
from utility.file_utils import simulate_send_email
from patterns.observer.observer import Observer
from email_validator import validate_email, EmailNotValidError

class Client(Observer):
    """
    Represents a client, storing their personal details and email information.
    """
    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        """
        Initializes a new Client instance with provided details.

        
        Args:
            client_number (int): A unique identifier for the client.
            first_name (str): The client's first name.
            last_name (str): The client's last name.
            email_address (str): The client's email address.

            
        Raises:
            ValueError: If the client number is not an integer, or if the first or last name is empty.
            EmailNotValidError: If the provided email address is invalid.
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
            validated_email = validate_email(email_address, check_deliverability=False)
            self.__email_address = validated_email.normalized
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"

    @property
    def client_number(self) -> int:
        """
        Retrieves the client's unique identifier.

        Returns:
            int: The client’s number.
        """
        return self.__client_number
    
    @property
    def first_name(self) -> str:
        """
        Retrieves the client's first name.

        Returns:
            str: The client's first name.
        """
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        """
        Retrieves the client's last name.

        Returns:
            str: The client's last name.
        """
        return self.__last_name
    
    @property
    def email_address(self) -> str:
        """
        Retrieves the client's email address.

        Returns:
            str: The client's email address.
        """
        return self.__email_address
    
    def __str__(self):
        """
        Returns a string representation of the client.

        Returns:
            str: A formatted string with the client's details.
        """
        return f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_address}"
    
    def update(self, message: str):
        """
        Notified when an update occurs. Sends an email with the update message.
        
        Args:
            message (str): The update message to be sent in the email.
        """
        current_time = datetime.now()
        subject = f"ALERT: Unusual Activity: {current_time}"
        email_message = f"Notification for {self.client_number}: {self.first_name} {self.last_name}: {message}"
        
        simulate_send_email(self.email_address, subject, email_message)
