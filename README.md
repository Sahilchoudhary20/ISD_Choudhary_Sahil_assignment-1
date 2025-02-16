# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Sahil Choudhary

## Assignment
Assignment : 1 - In this assignment i will leverage the knowledge gained in Module 01 to develop classes to support a larger system. This is the first of many assignments in this course, each of which will build on the previous assignment in order to produce a complete system. The focus of this assignment aligns with the focus of the first module - that is, classes, encapsulation and unit test planning.

Assignment : 2 - This assignment will extend the BankAccount class created in your previous assignment. The BankAccount class will be used as a superclass from which more specific subclasses will be derived. Each subclass will inherit attributes and methods from the superclass, and will incorporate functionality specific to the subclass. Polymorphism will be realized by having each subclass provide their own unique implementation to a superclass method. Unit testing in this assignment will be limited to verifying the expected polymorphic behaviour.

## Encapsulation
Private Attributes:

The class uses private attributes by prefixing them with double underscores (__). For example, self.__account_number, self.__client_number, and self.__balance are all private.
These private attributes cannot be directly accessed or modified from outside the class, ensuring that the internal data is protected and cannot be changed arbitrarily.

Public Methods (Accessors and Mutators):

Getter methods (accessors): The @property decorators are used to create read-only accessors for the private attributes. For instance:
account_number, client_number, and balance are accessed through their respective getter methods, which return the value of the private attributes.
Setter methods (mutators): The class provides methods like deposit, withdraw, and update_balance to modify the balance attribute. These methods perform checks (such as ensuring positive amounts or validating data types) before allowing any changes to the balance, enforcing business logic.

Controlled Modification:

The balance is modified only through methods (such as deposit, withdraw, and update_balance). This ensures that any changes to the balance occur under controlled conditions, like ensuring the withdrawal amount doesn’t exceed the available balance, or deposits are positive and numeric.
This prevents the direct modification of the __balance attribute from external code, ensuring that the account state remains consistent and valid according to the rules defined in the class.