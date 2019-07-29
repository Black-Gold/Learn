# **extundelete**

用法：extundelete [options] [--] device-file

```info
  --superblock           Print contents of superblock in addition to the rest.
                         If no action is specified then this option is implied.
  --journal              Show content of journal.
  --after dtime          Only process entries deleted on or after 'dtime'.
  --before dtime         Only process entries deleted before 'dtime'.
Actions:
  --inode ino            Show info on inode 'ino'.
  --block blk            Show info on block 'blk'.
  --restore-inode ino[,ino,...]
                         Restore the file(s) with known inode number 'ino'.
                         The restored files are created in ./RECOVERED_FILES
                         with their inode number as extension (ie, file.12345).
  --restore-file 'path'  Will restore file 'path'. 'path' is relative to root
                         of the partition and does not start with a '/'
                         The restored file is created in the current
                         directory as 'RECOVERED_FILES/path'.
  --restore-files 'path' Will restore files which are listed in the file 'path'.
                         Each filename should be in the same format as an option
                         to --restore-file, and there should be one per line.
  --restore-directory 'path'
                         Will restore directory 'path'. 'path' is relative to the
                         root directory of the file system.  The restored
                         directory is created in the output directory as 'path'.
  --restore-all          Attempts to restore everything.
  -j journal             Reads an external journal from the named file.
  -b blocknumber         Uses the backup superblock at blocknumber when opening
                         the file system.
  -B blocksize           Uses blocksize as the block size when opening the file
                         system.  The number should be the number of bytes.
  --log 0                Make the program silent.
  --log filename         Logs all messages to filename.
--log D1=0,D2=filename   Custom control of log messages with comma-separated
   Examples below:       list of options.  Dn must be one of info, warn, or
   --log info,error      error.  Omission of the '=name' results in messages
   --log warn=0          with the specified level to be logged to the console.
   --log error=filename  If the parameter is '=0', logging for the specified
                         level will be turned off.  If the parameter is
                         '=filename', messages with that level will be written
                         to filename.
   -o directory          Save the recovered files to the named directory.
                         The restored files are created in a directory
                         named 'RECOVERED_FILES/' by default.
```

