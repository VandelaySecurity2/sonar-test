class MyClass:
    pass

# DEBUG-Solar Bug #1
myvar = MyClass()
myvar()  # Noncompliant

none_var = None
# DEBUG-Solar Bug #2
none_var()  # Noncompliant

# DEBUG-Solar Code Smell #1
exec 'print 1'  # Noncompliant






# DEBUG-Solar Code Smell #2
raise  # Noncompliant

def foo():
    # DEBUG-Solar Code Smell #3
    raise  # Noncompliant
    try:

        # DEBUG-Solar Code Smell #4
        raise  # Noncompliant
    except ValueError as e:
        handle_error()
    except:
        raise
    else:
        # DEBUG-Solar Code Smell #5
        raise  # Noncompliant
    finally:
        raise

def handle_error():
    # DEBUG-Solar Code Smell #6
    raise  # Noncompliant. This works but is hard to understand.





{"one": 1, "two": 2, "one": 3}  # Noncompliant

def func(a1, a2, a3):
    {a1: 1, a2: 2, a1: 3}  # Noncompliant.

    username = 'admin'
    password = 'admin'  # Sensitive
    usernamePassword = 'user=admin&password=admin'  # Sensitive

import os

def send_signal(pid, sig, pgid):
    os.kill(pid, sig)  # Sensitive
    os.killpg(pgid, sig)  # Sensitive