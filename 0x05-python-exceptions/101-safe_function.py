#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    strmen = "Exception: "
    try:
        result = fct(*args)  # passing arguments to function
        return result
    except (ZeroDivisionError, IndexError) as men:
        strmen += str(men)
        strmen += "\n"
        sys.stderr.write(strmen)
        return None
