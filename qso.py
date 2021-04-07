# The following Python code defines an abstraction barrier 
# and a possible representation for a QSO:
# QSO with data abstraction:
def makeqso(time, call): # constructor
    return [time, call]
def gettime(qso):   # selector
    return qso[0]    
def getcall(qso):   # selector
    return qso[1]

# The barrier consists of constructors and selectors.
# These separate the use from the representation. Example usage:
# Example usage:
foo = makeqso('18:35', 'SK7MW')
print(getcall(foo))

# In this example, we have only used the abstraction barrier.
# Nothing in the example shows how the QSO is actually represented internally.
# That is, if we had chosen an alternative representation, see below, 
# the usage of the object would remain exactly the same.
# The functions makeqso, gettime and getcall form the abstraction barrier 
# which means that the representation is hidden behind these functions.
# Any implementationf of QSO which fullfills 

# gettime(makeqso(time, call)) = time
# and
# getcall(makesqso(time, call)) = call

# is a valid implementation,
# i.e. we have defined our abstraction barrier, also called interface.
# Here is an alternative (harder to understand) representation:

def makeqso(time, call): # constructor
    return lambda pick: time if pick else call 
def gettime(qso):   # selector
    return qso(True)    
def getcall(qso):   # selector
    return qso(False)

# However the above example for using the interface works exactly in the same way.
# That is, the code in the exactly does not need any changes in order to work with our alternative representation.
# WITHOUT DATA ABSTRACTION
# Next, let's look at the code if we had not used data abstraction:
# QSO without data abstraction:
foo = ['18:35', 'SK7MW']
print(foo[1])
# That's all the code, we can perfectly do this without data abstraction
# it's even shorter. So what?
# Why don't we do it the simple this way?
# Without data abstraction, it is:
# Very straightforward.
# There are fewer things to define, hence shorter code.
# We are saved from having to worry about the concept of data abstraction.
# It will almost certainly excecute faster.

# One of the principles of computing states that
# everything should be as simple as possible, 
# and now we have introduced the concept of data abstraction,
# and made things more complicated.
# Why in heavens name should we use data abstraction?
# What is the real advantage of using data abstraction?

# The advantage
# The real advantage is that we could choose a different representation without changing the user code.
# This is very important because at the moment we write the interface, 
# we might not know what the best representation is.
# we can write the interface and pretend we already have a representation.
# Like stated above, any implementation which fulfills the specifications will do the job.
# This means that once we have defined the interface, we can move on and not worry about the representation, 
# or have somebody else worry about the representation.
# when faced with a common problem, we can even look for interfaces what have been defined already
# and not worry about the representation al all!
# This is the real power and flexibility of data abstraction. 

# A class inteface
# The example above is trivial and no real Python programmer would create the constructor and selectors this way.
# For a problem like this on Python offers classes which make the code more readable.

class QSO:
    def __init__(self, time, call):  # constructor
        self.time = time
        self.call = call
# we simply select the attributes directly, so we don't need to write extra code for the selectors.
# Our abstraction barrier (interface) can now be expresesed as:
# 
# QSO(time, call).time = time
# and
# QSO(time, call).call = call
# Note that time and call are used as both variables and attributes in the definition.
# Again, here is how one can use the class, oops!, I meant abstraction barrier.
#  a QSO with data abstraction as a class instance:
foo = QSO('18:35', 'SK7MW')

# e.g.: to get the call we say
print(foo.call)     
# As seen from this example, data abstraction does not require the use of classes.
# One can achieve the same thing with simple functions also.
# It is just that classes are very suited for creating abstraction interfaces.

# THE BOADER PICTURE
# It is possible to use data abstraction in any programming language,
# making use of this technique will lead to to more reliable programs,
# and (as long as the abstraction is well documented and defined) easier to read software, 
# because a seemingly complicated task can be broken down into its natural pieces,
# and each piece can be analyzed by itself.
# Finding the right abstraction barrier for a given problem is the hard part, 
# and requires programming practice and experience
# Data abstraction goes far beyond creating structures which contain other things.
# In fact, data abstraction is a very general technique which is used throughout engineering, not just software engineering.

# In programming, structures are data abstractions on a low level, on the next level are objects with methods,
# this is usually called objects oriented programming. On an even higher level, data abstraction is used to create programming languages. 
# Here the abstraction barrier is the programming language, (e.g. Python, C, Java), and the representation the implementation of the language. 
# Just like in our trivial example, one might change the representation, that is use a different language compiler or interpreter. 
# As long as the interface (e.g. Java) is well defined code written for one compiler will also run on another. 