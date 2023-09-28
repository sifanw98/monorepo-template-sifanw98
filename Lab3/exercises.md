# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- *It is a concrete class. Even though this class does not contain any methods or constructors, it can be instatiated without errors since it does not contain abstract methods.*
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- *It is a special method that defines the behavior when an instance of the class is about to be deleted or destroyed.*
1. What class does Texture inherit from?
	- *It inherits from the Image class.*
1. What methods and attributes does the Texture class inherit from 'Image'? 
	- *Methods include: '__init__', 'getWidth', 'getHeight', 'getPixels', 'setPixelsToRandomValue'*
	- *Attributes include: m_width, m_height, m_colorChannels, m_Pixels*
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- *I think it should have a 'has-a' relationship since texture isn't strictly an image by itself. The code is refracted to a 'has-a' relationship.*
1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- *Even though it does not have a constructor. It will automatically create a constructor since it if a child class of Image class.*

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

*It is not safe, as in if multiple threads are trying to create an instance at the same time. It is possible that multiple instances will be created.*  
  
