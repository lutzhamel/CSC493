section .data
    x dw 1
    y dw 2

section .bss
    z resw 1

section .text
    global _start

_start:
    mov ax, [x]    ; fetch x
    add ax, [y]    ; fetch and add y
    mov [z], ax    ; store result in z

    ; exit the program
    mov eax, 1
    xor ebx, ebx
    int 0x80

