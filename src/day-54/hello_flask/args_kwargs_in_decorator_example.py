class User:

    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper_function(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper_function

@is_authenticated_decorator
def create_blog_post(user):
    print(f"New blog post created by {user.name}!!")


user = User("Aditya")
user.is_logged_in = True
create_blog_post(user)


inputs = eval(input("enter 3 coma seperated numbers:"))
# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
  def wrapper_function(*args, **kwargs):
    output = function(args[0], args[1], args[2])
    print(f"You called {function.__name__}{args}")
    print(f"It returned: {output}")
  return wrapper_function


# TODO: Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
  return a * b * c

a_function(inputs[0], inputs[1], inputs[2])