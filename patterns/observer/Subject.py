"""This module defines the Subject class for implementing the Observer pattern."""

__author__ = "Sahil Choudhary"
__version__ = "1.0.0"

"""
Subject class for implementing the Observer pattern.
"""

from abc import ABC, abstractmethod
from patterns.observer.observer import Observer

class Subject(ABC):
    """
    Abstract class for subjects in the Observer pattern.
    
    This class maintains a list of observers and provides methods
    to attach, detach, and notify them of changes.
    """
    
    def __init__(self):
        """
        Initialize a new Subject instance with an empty list of observers.
        """
        self._observers = []
    
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to this subject.
        
        Args:
            observer (Observer): The observer to attach.
        """
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from this subject.
        
        Args:
            observer (Observer): The observer to detach.
        """
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self, message: str) -> None:
        """
        Notify all attached observers of a change.
        
        Args:
            message (str): A message describing the change.
        """
        for observer in self._observers:
            observer.update(message)