# nm

## 说明

**nm命令** 被用于显示二进制目标文件的符号表

## 选项

```markdown
用法：nm [选项] [文件]
列举 [文件] 中的符号 (默认为 a.out)

-a, --debug-syms       Display debugger-only symbols
-A, --print-file-name  在每个符号之前打印输入文件的名称
-B                     Same as --format=bsd
-C, --demangle[=STYLE] Decode low-level symbol names into user-level names
                        The STYLE, if specified, can be `auto' (the default),
                        `gnu', `lucid', `arm', `hp', `edg', `gnu-v3', `java'
                        or `gnat'
    --no-demangle      Do not demangle low-level symbol names
-D, --dynamic          显示动态符号 
    --defined-only     Display only defined symbols
-e                     (ignored)
-f, --format=FORMAT    Use the output format FORMAT.  FORMAT can be `bsd',
                         `sysv' or `posix'.  The default is `bsd'
-g, --extern-only      只显示外部符号
-l, --line-numbers     Use debugging information to find a filename and
                         line number for each symbol
-n, --numeric-sort     Sort symbols numerically by address
-o                     Same as -A
-p, --no-sort          Do not sort the symbols
-P, --portability      Same as --format=posix
-r, --reverse-sort     反序显示符号表 
    --plugin NAME      Load the specified plugin
-S, --print-size       Print size of defined symbols
-s, --print-armap      Include index for symbols from archive members
    --size-sort        Sort symbols by size
    --special-syms     Include special symbols in the output
    --synthetic        Display synthetic symbols as well
-t, --radix=RADIX      Use RADIX for printing symbol values
    --target=BFDNAME   Specify the target object format as BFDNAME
-u, --undefined-only   Display only undefined symbols
-X 32_64               (ignored)
@FILE                  Read options from FILE

nm：支持的目标： elf64-x86-64 elf32-i386 elf32-iamcu elf32-x86-64 a.out-i386-linux pei-i386 pei-x86-64 elf64-l1om 
elf64-k1om elf64-little elf64-big elf32-little elf32-big plugin srec symbolsrec verilog tekhex binary ihex

```

## 实例 

