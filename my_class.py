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


from OpenSSL import SSL

SSL.Context(SSL.SSLv3_METHOD)  # Noncompliant

import ssl

ssl.SSLContext(ssl.PROTOCOL_SSLv3) # Noncompliant

import ldap

def init_ldap():
   connect = ldap.initialize('ldap://example:1389')

   connect.simple_bind('cn=root') # Noncompliant
   connect.simple_bind_s('cn=root') # Noncompliant
   connect.bind_s('cn=root', None) # Noncompliant
   connect.bind('cn=root', None) # Noncompliant

# just a comment
# another comment
# another comment
# another comment
# another comment
# another comment