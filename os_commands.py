import os


# DEBUG-Sonar Vulnerability #1
def ping():
    cmd = "ping 8.8.8.8"
    os.popen(cmd)  # Noncompliant
