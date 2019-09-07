# readelf

## 说明

**readelf命令** 用来显示一个或者多个elf格式的目标文件的信息，可以通过它的选项来控制显示哪些信息。这里的elf-file(s)就表示
那些被检查的文件。可以支持32位，64位的elf格式文件，也支持包含elf文件的文档（这里一般指的是使用ar命令将一些elf文件打包之
后生成的例如lib*.a之类的“静态库”文件）

这个程序和objdump提供的功能类似，但是它显示的信息更为具体，并且它不依赖BFD库(BFD库是一个GNU项目，它的目标就是希望通过一
种统一的接口来处理不同的目标文件)，所以即使BFD库有什么bug存在的话也不会影响到readelf程序

运行readelf的时候，除了-v和-H之外，其它的选项必须有一个被指定

## 选项

```markdown
用法：readelf <选项> elf-文件
 显示关于 ELF 格式文件内容的信息
 Options are:
  -a --all               显示全部信息,等价于: -h -l -S -s -r -d -V -A -I
  -h --file-header       显示elf文件开始的文件头信息
  -l --program-headers   Display the program headers
     --segments          An alias for --program-headers
  -S --section-headers   Display the sections' header
     --sections          An alias for --section-headers
  -g --section-groups    Display the section groups
  -t --section-details   Display the section details
  -e --headers          显示全部头信息,等价于: -h -l -S
  -s --syms              Display the symbol table
     --symbols           An alias for --syms
  --dyn-syms             Display the dynamic symbol table
  -n --notes             Display the core notes (if present)
  -r --relocs            显示可重定位段的信息 (if present)
  -u --unwind            显示unwind段信息。当前只支持IA64 ELF的unwind段信息 (if present)
  -d --dynamic           Display the dynamic section (if present)
  -V --version-info      Display the version sections (if present)
  -A --arch-specific     Display architecture specific information (if any)
  -c --archive-index     Display the symbol/file index in an archive
  -D --use-dynamic       Use the dynamic section info when displaying symbols
  -x --hex-dump=<number|name>
                         Dump the contents of section <number|name> as bytes
  -p --string-dump=<number|name>
                         Dump the contents of section <number|name> as strings
  -R --relocated-dump=<number|name>
                         Dump the contents of section <number|name> as relocated bytes
  -z --decompress        Decompress section before dumping it
  -w[lLiaprmfFsoRt] or
  --debug-dump[=rawline,=decodedline,=info,=abbrev,=pubnames,=aranges,=macro,=frames,
               =frames-interp,=str,=loc,=Ranges,=pubtypes,
               =gdb_index,=trace_info,=trace_abbrev,=trace_aranges,
               =addr,=cu_index]
                         Display the contents of DWARF2 debug sections
  --dwarf-depth=N        Do not display DIEs at depth N or greater
  --dwarf-start=N        Display DIEs starting with N, at the same depth
                         or deeper
  -I --histogram         Display histogram of bucket list lengths
  -W --wide              Allow output width to exceed 80 characters
  @<file>                Read options from <file>

```

### ELF文件类型

 **种类型的ELF文件：** 

1.  可重定位文件:用户和其他目标文件一起创建可执行文件或者共享目标文件,例如lib*.a文件。 
2.  可执行文件：用于生成进程映像，载入内存执行,例如编译好的可执行文件a.out。 
3.  共享目标文件：用于和其他共享目标文件或者可重定位文件一起生成elf目标文件或者和执行文件一起创建进程映像，例如lib*.so文件。 

 **ELF文件作用：** 

ELF文件参与程序的连接(建立一个程序)和程序的执行(运行一个程序)，所以可以从不同的角度来看待elf格式的文件： 

1.  如果用于编译和链接（可重定位文件），则编译器和链接器将把elf文件看作是节头表描述的节的集合,程序头表可选。 
2.  如果用于加载执行（可执行文件），则加载器则将把elf文件看作是程序头表描述的段的集合，一个段可能包含多个节，节头表可选。 
3.  如果是共享文件，则两者都含有。 

 **ELF文件总体组成：**  

elf文件头描述elf文件的总体信息。包括：系统相关，类型相关，加载相关，链接相关。 

*   系统相关表示：elf文件标识的魔术数，以及硬件和平台等相关信息，增加了elf文件的移植性,使交叉编译成为可能。 
*   类型相关就是前面说的那个类型。 
*   加载相关：包括程序头表相关信息。 
*   链接相关：节头表相关信息。 

## 实例

```bash
readelf -h main         # 读取可执行文件main的elf文件头信息
readelf -h myfile.o     # 读取目标文件形式的elf文件头信息
readelf -h libmy.a      # 读取静态库文件形式的elf文件头信息
readelf -h libmy.so     # 读取动态库文件形式的elf文件头信息 
readelf -l main         # 查看可执行的elf文件程序头表信息
readelf -l myfile.o     # 查看目标文件的elf文件程序头表信息
readelf -l libmy.a      # 查看静态库文件的elf文件程序头表信息
readelf -l libmy.so     # 查看动态库文件的elf文件程序头表信息
readelf -S main         # 查看一个可执行的elf文件的节信息
readelf -S main.debug   # 查看一个包含调试信息的可执行的elf文件的节信息
readelf -S myfile.o     # 查看一个目标文件的elf文件的节信息
readelf -S libmy.a      # 查看一个静态库文件的elf文件的节信息

```
