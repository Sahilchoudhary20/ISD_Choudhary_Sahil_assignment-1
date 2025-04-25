"""This module defines the Observer pattern class."""

__author__ = "Sahil Choudhary"
__version__ = "1.1.0"

"""
Observer interface for implementing the Observer pattern.
"""

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Abstract base class for all observers in the Observer pattern.
    
    Classes that implement this interface will be notified of changes
    by subjects they are observing.
    """
    
    @abstractmethod
    def update(self, message: str):
        """
        Method called when a subject this observer is watching changes state.
        
        Args:
            message (str): A message describing the change that occurred.
        """
        pass
