# objdump

## 说明

**objdump命令** 是用查看目标文件或者可执行的目标文件的构成的gcc工具。显示二进制文件信息

## 选项

```markdown
用法：objdump <选项> <文件>
 显示来自目标 <文件> 的信息。至少必须给出以下选项之一：
-a, --archive-headers    Display archive header information
-f, --file-headers       Display the contents of the overall file header
-p, --private-headers    Display object format specific file header contents
-P, --private=OPT,OPT... Display object format specific contents
-h, --[section-]headers  Display the contents of the section headers
-x, --all-headers        Display the contents of all headers
-d, --disassemble        Display assembler contents of executable sections
-D, --disassemble-all    Display assembler contents of all sections
-S, --source             Intermix source code with disassembly
-s, --full-contents      Display the full contents of all sections requested
-g, --debugging          Display debug information in object file
-e, --debugging-tags     Display debug information using ctags style
-G, --stabs              Display (in raw form) any STABS info in the file
-W[lLiaprmfFsoRt] or
--dwarf[=rawline,=decodedline,=info,=abbrev,=pubnames,=aranges,=macro,=frames,
        =frames-interp,=str,=loc,=Ranges,=pubtypes,
        =gdb_index,=trace_info,=trace_abbrev,=trace_aranges,
        =addr,=cu_index]
                         Display DWARF info in the file
-t, --syms               Display the contents of the symbol table(s)
-T, --dynamic-syms       Display the contents of the dynamic symbol table
-r, --reloc              Display the relocation entries in the file
-R, --dynamic-reloc      Display the dynamic relocation entries in the file
@<file>                  Read options from <file>
-v, --version            Display this program's version number
-i, --info               List object formats and architectures supported
-H, --help               Display this information

 以下选项是可选的：
-b, --target=BFDNAME           将标的目标文件格式指定为 BFDNAME
-m, --architecture=MACHINE     将标的体系结构指定为 MACHINE
-j, --section=NAME             只显示 NAME 节的信息
 isassembler-options=OPT 将文本传递到 OPT 反汇编程序
 ian=big               反汇编时假定高位字节在前
 ian=little            反汇编时假定低位字节在前
    --file-start-context       从文件的起点引入上下文 (带有 -S)
-l, --line-numbers             在输出中给出行号和文件名
 emangle[=STYLE]         对修饰过的 (mangled) 符号名进行解码
                                如果给出了 STYLE，STYLE 可能为“auto”、“gnu”、
 ”、“arm”、“hp”、“edg”或“gnu-new-abi”
 e                     以多于 80 列的宽度对输出进行格式化
 isassemble-zeroes       反汇编时不要跳过为零的块
 dress=ADDR       只有进程数据的地址 >= ADDR
 dress=ADDR        只有进程数据的地址 <= ADDR
 dresses         同反汇编代码并列显示完整的地址
    --[no-]show-raw-insn       同符号反汇编并列显示十六进制值
 just-vma=OFFSET        为所有显示的节地址增加 OFFSET

 warf-depth=N        Do not display DIEs at depth N or greater
 warf-start=N        Display DIEs starting with N, at the same depth
 eeper
 warf-check          Make additional dwarf internal consistency checks.      

objdump：支持的目标： elf64-x86-64 elf32-i386 elf32-iamcu elf32-x86-64 a.out-i386-linux pei-i386 pei-x86-64 elf64-l1om elf64-k1om elf64-little elf64-big elf32-little elf32-big plugin srec symbolsrec verilog tekhex binary ihex
objdump：支持的体系结构： i386 i386:x86-64 i386:x64-32 i8086 i386:intel i386:x86-64:intel i386:x64-32:intel i386:nacl i386:x86-64:nacl i386:x64-32:nacl iamcu iamcu:intel l1om l1om:intel k1om k1om:intel plugin

下列 i386/x86-64 特定的反汇编器选项在使用 -M 开关时可用（使用逗号分隔多个选项）：
  x86-64      Disassemble in 64bit mode
  i386        Disassemble in 32bit mode
  i8086       在 16 位模式下反汇编
  att         用 AT&T 语法显示指令
  intel       用 Intel 语法显示指令
  att-mnemonic
              Display instruction in AT&T mnemonic
  intel-mnemonic
              Display instruction in Intel mnemonic
  addr64      假定 64 位地址大小
  addr32      假定 32 位地址大小
  addr16      假定 16 位地址大小
  data32      假定 32 位数据大小
  data16      假定 16 位数据大小
  suffix      在 AT&T 语法中始终显示指令后缀
  amd64       Display instruction in AMD64 ISA
  intel64     Display instruction in Intel64 ISA

```

## 实例

```bash
objdump -a libmy2.a     # 查看档案库文件中的信息
objdump -i          # 显示可用的架构和目标结构列表
objdump --section=.text -s mytest.o     # 显示mytest.o文件中的text段的内容
objdump -S mytest.o   # 反汇编出mytest.o的源代码

objdump -j .text -S mytest.o
: << comment
反汇编mytest.o中的text段内容，并尽可能用源代码形式表示,注意:不能单独使用-j或者--section，例如`objdump -j .text mytest.o
是不会运行成功的`。另外-S命令对于包含调试信息的目标文件，显示的效果比较好如果编译时没有指定g++的-g选项，那么目标文件就不
包含调试信息
comment

objdump -d -l mytest.o
: << comment
反汇编特定段，并将汇编代码对应的文件名称和行号对应上
这里，项"-d"从objfile中反汇编那些特定指令机器码的section，而使用"-l"指定用文件名和行号标注相应的目标代码，仅仅和-d、-D或
者-r一起使用，使用-ld和使用-d的区别不是很大，在源码级调试的时候有用，要求编译时使用了-g之类的调试编译选项
comment

```

