# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

*I think these names do correlate what they do. I think this question is more about established conventions. Most of the function names are also used in other languages' standard library. Changing "pop" to "popAndGet" should be unnecessary and may cause some confusion.*

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

*Dictionary uses hashed structure with key-value pairs and is not ordered, while lists are used to store data like array and are ordered and sequential.*

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

*Yes, it does. Such syntax is also allowed. *

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

*Pros: There are a lot of flexibility when choosing the container, which is also very easy for developing.*
*Cons: However, such dynamic nature can result in type complexity where bugs might occur if type of data is not checked.*

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

*Yes, these functions are well-named. The function name contains the verbs that correctly represents the actions of the function.*

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

*Indeed, some of the functions do have a lot of parameters. However, some of the parameters already have default values and are optional.*

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

*'**kwargs' are optional arguments that request take. It is good for flexibility, meaning that it is not forcing users to pass multiple arguments everytime. However, like the last question suggested, it might be prone to errors when users made typos in keywords and the typos are hard to find since they are not checked by being optional.*

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?


*Normally, the argument set to none is a mutable data object like dictionary, list of typles, bytes. Setting the argument default to be none can ensure that the object is surely created if the user forgets to include the data and causes errors. Arguments can be set to other things, while it might not be a good practice in this case, since the data objects are often mutable and are used differently. It is good to avoid problems of missing arguments and also good to avoid problems for exiting function calls if the argument is newly added.*
