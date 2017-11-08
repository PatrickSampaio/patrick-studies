###OOP On Python

#ClassMethods

The principal use of ClassMethods, is to make an alternative constructor. This method, he is oriented by class instead of by instance, like a normal methods is.
The first argument of an function MUST be an cls, cls stands for class
`@classmethod`

#StaticMethods

StaticMethod is an method that doesn't work with an class nor an instance, it's an normal function inside an class

`@staticmehod`

##Inheritance

`print(help(Developer))`

Help on class Developer in module __main__:

class Developer(Employee)
 |  Methods inherited from Employee:
 |  
 |  __init__(self, first, last, pay)
 |  
 |  apply_raise(self)
 |  
 |  fullname(self)
 |  
 |  ----------------------------------------------------------------------
 |  Class methods inherited from Employee:
 |  
 |  set_raise_amt(cls, amount) from __builtin__.classobj


You can use Base Class's methods on the derived class

`def __init__(self, fist, last, pay, prog_lang):
        self.prog_lang = prog_lang
        super().__init__(first, last, pay)`

