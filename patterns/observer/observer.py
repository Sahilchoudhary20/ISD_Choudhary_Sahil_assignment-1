"""This module defines the Observer pattern class."""

__author__ = "Sahil Choudhary"
__version__ = "1.1.0"

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Abstract base class for observers in the Observer pattern.
    
    Defines the interface for receiving update notifications.
    """
    
    @abstractmethod
    def update(self, message: str) -> None:
        """
        Abstract method for processing update notifications.
        This method should be implemented by subclasses.

        Args:
            message (str): The notification message with updated information.
        """
        pass
