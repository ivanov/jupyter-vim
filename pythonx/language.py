"""
Jupyter language interface for vim client:
"""

# Export only: see at end
__all__ = ['list_languages', 'get_language']


class Language:
    """Language Base"""
    prompt_in = 'In [{line:d}]: '
    prompt_out = 'Out[{line:d}]: '
    print_string = 'print("{}")'
    cd = 'cd "{}"'
    pid = -1
    cwd = '"unknown"'
    hostname = '"unknown"'


class Bash(Language):
    prompt_in = 'Sh [{line:d}]: '
    print_string = 'echo -e "{}"'
    cd = 'cd "{}"'
    pid = '_res=$$; echo $_res;'
    cwd = '_res=$(pwd); echo $_res;'
    hostname = '_res=$(hostname); echo $_res;'


class Javascript(Language):
    prompt_in = 'Js [{line:d}]: '
    print_string = 'console.log("{}");'
    cd = 'require("process").chdir("{}");'
    pid = '_res = require("process").pid;'
    cwd = '_res = require("process").cwd();'
    hostname = '_res = require("os").userInfo().username;'


class Julia(Language):
    prompt_in = 'Jl [{line:d}]: '
    print_string = 'println("{}")'
    cd = 'cd "{}"'
    pid = '_res = getpid()'
    cwd = '_res = pwd()'
    hostname = '_res = gethostname()'


class Perl(Language):
    prompt_in = 'Pl [{line:d}]: '
    print_string = 'print("{}")'
    cd = 'chdir("{}")'
    pid = '$_res = $$'
    cwd = 'use Cwd; $_res = getcwd();'
    hostname = 'use Sys::Hostname qw/hostname/; $_res = hostname();'


class Python(Language):
    prompt_in = 'Py [{line:d}]: '
    print_string = 'print("{}")'
    cd = '%cd "{}"'
    pid = 'import os; _res = os.getpid()'
    cwd = 'import os; _res = os.getcwd()'
    hostname = 'import socket; _res = socket.gethostname()'


class Ruby(Language):
    prompt_in = 'Rb [{line:d}]: '
    print_string = 'print("{}")'
    cd = '_res = Dir.chdir "{}"'
    pid = '_res = Process.pid'
    cwd = '_res = Dir.pwd'
    hostname = '_res = Socket.gethostname'


# Dict: kernel_type -> class
language_dict = {
    'bash': Bash,
    'javascript': Javascript,
    'julia': Julia,
    'perl': Perl,
    'python': Python,
    'ruby': Ruby,
}


def list_languages():
    return language_dict.keys()


def get_language(kernel_type):
    """Get language class
    Assert that language is in language_list (checked by caller)
    But still, let's return something
    """
    if kernel_type not in list_languages():
        return Language
    return language_dict[kernel_type]