"""This module contains functions related to Jupyter notebooks 
on the rhodes-notebook.org environment.
"""

import ast
import types
import sys
from client.api.notebook import Notebook
from IPython.display import display, Markdown, Latex

# The ok control variable.
_ok = None

def ok_login(okfile):
    """Authenticate to the OK submission website.
    This is a wrapper around creating a Notebook object and calling auth().
    
    okfile: the .ok file that describes the OK assignment we are using.
    """
    
    global _ok
    _ok = Notebook(okfile)
    _ok.auth(inline=True)
    
def ok_runtests(okfile, question):
    """Run test cases and grade them using OK.
    
    okfile: the .ok file that describes the OK assignment we are using.
    question: the test file to use.
    """
    
    global _ok
    if _ok == None:
        ok_login(okfile)
    _ok.grade(question)
    
def ok_submit(okfile):
    """Submit the current notebook and auxiliary files specified in the .ok file.
    
    okfile: the .ok file that describes the OK assignment we are using.
    """
    
    global _ok
    if _ok == None:
        ok_login(okfile)
    _ok.submit()
    display(Markdown('<font size=+1>⚠️ To make sure your submission was successful, '
                     + 'make sure there are no error messages in the output above, and '
                     + 'then click on the URL '
                     + ' to make sure your submission looks correct. ⚠️</font>'))

def reload_functions(filename, verbose=False):
    """Import/re-import all functions from a filename into the __main__ namespace.  
    Python typically ignores subsequent import commands after the first one, this
    function forces the specified file to be re-read and re-imported.  However, 
    any function *calls* are ignored.  
    
    This function came about for two reasons.  First, we typically have students
    call main() at the end of their programs, and when one does "from ___ import *"
    that will end up calling main() when all you want to do is import the functions
    into a notebook so they can be tested.  Furthermore, the IPython %autoreload magic
    is buggy at times, and doesn't always seem to reload the functions, and when it
    does, it still ends up calling main().  Hence this function was designed to solve
    both of those problems: it effectively executes the given Python file in the
    __main__ namespace, but ignores any function calls.  Therefore, function definitons,
    other imports, and global variables/constants will be imported correctly into the
    main notebook space.

    In a notebook cell, one can put:

    from cs1.notebooks import *
    reload_functions("student_project_file.py")

    and then all the functions in the .py file should be available in that notebook
    cell, and any calls to main() or other functions in the .py file will be ignored.
    """
    
    if verbose: print("Reloading functions from", filename)

    with open(filename) as f:
        p = ast.parse(f.read(), filename=filename)

        for node in p.body[:]:
            #if not isinstance(node, ast.FunctionDef):
            #    p.body.remove(node)
            
            # accept everything except a function call
            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):   
                p.body.remove(node)
                if verbose: print("rejecting", node)
            else:
                if verbose: print("accepting", node)

    # Compile the code and add it to the __main__ dictionary, which contains
    # all the variables for the notebook cells.
    obj = compile(p, filename=filename, mode="exec")
    exec(obj, sys.modules["__main__"].__dict__)
    
