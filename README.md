# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Sahil Choudhary

## Assignment
Assignment : 1 - In this assignment i will leverage the knowledge gained in Module 01 to develop classes to support a larger system. This is the first of many assignments in this course, each of which will build on the previous assignment in order to produce a complete system. The focus of this assignment aligns with the focus of the first module - that is, classes, encapsulation and unit test planning.

Assignment : 2 - This assignment will extend the BankAccount class created in your previous assignment. The BankAccount class will be used as a superclass from which more specific subclasses will be derived. Each subclass will inherit attributes and methods from the superclass, and will incorporate functionality specific to the subclass. Polymorphism will be realized by having each subclass provide their own unique implementation to a superclass method. Unit testing in this assignment will be limited to verifying the expected polymorphic behaviour.

Assignment : 3 - This assignment will address issues associated with the scalability and maintainability of the current service charge calculation functionality. If PiXELL River Financial decided to add several new account types each with their own formula for calculating service charges, several issues could begin to arise such as bloated subclasses, duplication of functionality, and with each potential change to service charge policy, the need to update every subclass. As such, this current polymorphic solution is not scalable. In this assignment the Strategy Pattern will be applied to simplify and add scalability to the service charge functionality. In addition, the Observer Pattern will be introduced. Using the Observer Pattern a client will be notified whenever a large transaction takes place and/or whenever an account balance drops below a minimum value.

Assginment : 4 - I created a `ClientLookupWindow` class for this assignment that enables users to look up clients and see the bank accounts linked to them. In order to manage user interactions, like looking for clients and choosing accounts, I first set up the user interface and connected signals. The logic for verifying the client number, presenting the client's information, and displaying their accounts in a table was then put into practice. In order to guarantee a seamless user experience for managing client and account data, I lastly added functionality to update account details and handle events like account selection.

Assignment : 5 - In this assignment, I will integrate a filtering algorithm into the GUI application, allowing users to filter the bank account list based on custom criteria. Additionally, the project will be finalized by generating HTML help files for each class, based on the docstrings written throughout the semester. Finally, I will package the project into a user-friendly installer for easy distribution to users.

## Encapsulation
Private Attributes:

The class uses private attributes by prefixing them with double underscores (__). For example, self.__account_number, self.__client_number, and self.__balance are all private.
These private attributes cannot be directly accessed or modified from outside the class, ensuring that the internal data is protected and cannot be changed arbitrarily.

Public Methods:

Getter methods (accessors): The @property decorators are used to create read-only accessors for the private attributes. For instance:
account_number, client_number, and balance are accessed through their respective getter methods, which return the value of the private attributes.
Setter methods (mutators): The class provides methods like deposit, withdraw, and update_balance to modify the balance attribute. These methods perform checks (such as ensuring positive amounts or validating data types) before allowing any changes to the balance, enforcing business logic.

Controlled Modification:

The balance is modified only through methods (such as deposit, withdraw, and update_balance). This ensures that any changes to the balance occur under controlled conditions, like ensuring the withdrawal amount doesn’t exceed the available balance, or deposits are positive and numeric.
This prevents the direct modification of the __balance attribute from external code, ensuring that the account state remains consistent and valid according to the rules defined in the class.


## Polymorphism
Polymorphism in the subclasses of BankAccount is gained from the overriding of methods, in which each subclass (i.e. ChequingAccount, SavingsAccount, InvestmentAccount) provides its specific implementation of the get_service_charges() method. This means there can be several different ways to calculate service charges in the case of each type of account. By calling get_service_charges() on objects of different subclasses, we are able to treat these instances as a single entity in the form of BankAccount objects, and it is the correct method of each subclass being called during the runtime. This is the polymorphism that serves to allow flexible and dynamic manipulation. 

## Strategy Pattern
The Strategy Pattern in this application allows different service charge calculation methods for various bank account types to be defined and used interchangeably. Each strategy class implements a common interface, enabling flexible and maintainable code by encapsulating the calculation logic for each account type.

## Observer Pattern
In this application, the Observer Pattern is used to notify clients (observers) about changes in their bank accounts (subjects). The BankAccount class acts as the subject, managing a list of observers (clients) and notifying them of events like low balances or large transactions. The Client class, as the observer, receives these notifications and updates accordingly. The pattern ensures that clients are automatically informed of relevant account changes without directly coupling them to the bank account logic.


