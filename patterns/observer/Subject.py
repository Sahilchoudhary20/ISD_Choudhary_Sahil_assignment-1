"""This module defines the Subject class for implementing the Observer pattern."""

__author__ = "Sahil Choudhary"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from patterns.observer.observer import Observer

class Subject(ABC):
    """
    Abstract base class representing a Subject in the Observer pattern.

    This class manages a list of observers and provides methods for attaching, detaching,
    and notifying observers.
    """

    def __init__(self) -> None:
        """
        Initializes the subject with an empty list of observers.
        """
        self._observers = []

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Adds an observer to the subject's list of observers.

        Args:
            observer (Observer): The observer to be added to the list.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Removes an observer from the subject's list of observers.

        Args:
            observer (Observer): The observer to be removed from the list.
        """
        pass

    @abstractmethod
    def notify(self, message: str) -> None:
        """
        Sends a notification to all registered observers.

        Args:
            message (str): The message to be delivered to the observers.
        """
        pass
