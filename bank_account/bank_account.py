__author__ = "Sahil Choudhary"
__version__ = "1.0.0"
__credits__ = "Sahil Choudhary"

class Client:
    """
    Client class : Used to maintain client data
    """

    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        """
        To initialize the class attributes.

        Args:
            client_number (init):
            first_name (str):
            last_name (str):
            email_address (str):
        
        Returns:
                None

        Raises:
            valueError: When client_number is non-numneric, first_name is blank or last_name is blank.
            EmailNotValidError: When email_address is not in the correct format.    
        """

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number should be numeric.")
        
        if len(first_name.strip()) > 0:
            self.__first_name = first_name
        else:
            raise ValueError 
