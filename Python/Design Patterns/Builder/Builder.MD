## Builder Pattern

The Builder Pattern focus in on creating complex objects step-by-step.
The "director" invokes "builder" services as it interprets the external format. The "builder" creates part of the complex object each time it is called and maintains all intermediate state. When the product is built, the client retrieves the result form the builder
This pattern allows controler over the construction process. Unlike creational patterns that construct products in one shot, the Builder pattern constructs the product step by step under the controle of the "director"
