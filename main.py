# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
# def make_bold(func):
#     def wrap():
#         return f"<b>{func()}</b>"
#     return wrap
#
# def make_emp(func):
#     def wrap():
#         return "<em>" + func() + "</em>"
#     return wrap
#
# def underlined(func):
#     def wrap():
#         return "<u>" + func() + "</u>"
#     return wrap
#
#
# @app.route("/bye")
# @make_bold
# @make_emp
# @underlined
# def bye():
#     return "BYE!"
#
#
# if __name__ == "__main__":
#     app.run(debug=True)


# class User:
#     def __init__(self,name):
#         self.name = name
#         self.is_logged_in = False
#
# def is_authenticated(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in:
#             function(args[0])
#     return wrapper
#
# @is_authenticated
# def create_blog(user):
#     print(f"This is {user.name}'s new blog post.")
#
# @is_authenticated
# def hobbies(user):
#     print(f"{user.name}'s hobbies are: Basketball, football and photography")
#
#
# new_user = User("Prakash")
# new_user.is_logged_in = True
# create_blog(new_user)
# hobbies(new_user)


def logging_decorator(fn):
    def wrapper(*args, **kwargs):
        print(f"You called {fn.__name__}{args}")
        result = fn(args[0], args[1], args[2])
        print(f"It returned: {result}")

    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(1, 2, 3)
