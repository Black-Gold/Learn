#!/bin/bash
for file in *.md;
do
	mv -i "${file}" "${file/md/txt}"
done

#原理：
#${var/Pattern/Replacement}
#Pattern第一个匹配项，在var中替换为replacement
