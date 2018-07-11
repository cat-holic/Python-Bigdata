import sys


def greet_users(names):
    for i in names:
        users = i[0].upper() + i[1:]
        print("Hello, %s!" % users)


usernames = list(map(str, sys.argv[1:]))
greet_users(usernames)


