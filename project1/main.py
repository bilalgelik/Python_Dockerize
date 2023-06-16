import os


def print_env_variable():
    return os.getenv("Python_Dockerize")


print(print_env_variable())
