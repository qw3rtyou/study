import string
import sys


code = ""
sys.stdout.write("HSpace Mic-check :)\n")
sys.stdout.write("code: ")
sys.stdout.flush()
while True:
    line = sys.stdin.readline()
    if line.startswith("end"):
        break
    code += line

allowed = set(string.ascii_lowercase + "()[]: ._\n" + string.digits)

if allowed | set(code) != allowed:
    sys.stdout.write("nono :(\n")
elif len(code) > 0x80:
    sys.stdout.write("too long :(\n")
else:
    compiled = compile(code, "", "exec")
    eval(compiled, {"__builtins__": {}}, {"__builtins__": {}})
