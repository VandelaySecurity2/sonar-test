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