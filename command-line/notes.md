# Command line environment

### Job control
 - `man signal` : about signals for interruption
 - SIGINT  : ctrl + C
 - SIGQUIT : ctrl + \ 
 - SIGSTOP : ctrl + Z

### Terminal multiplexer

Structure:
 - Session
   - Windows (Tabs)
     - Panes

### Aliases
`alias gs="git status"`
`alias mv="mv -i"` (overwrite)

`alias mv` tells an alias of `mv`

### dot files
 - "~/.bashrc" for bash
 - "~/.vimrc" for vim
 - Search "dotfiles" on Github for resources.

### Remote control using SSH 
 - `ssh (user)@(host) (some commands)`
 - `scp (file) user@host:(new file)

### Exercises

### Job control

1. pgrep and pkill
```sh
$ sleep 10000 &
[1] ****
$ pkill sleep
[1] terminated ...
```
> I don't need pid with 'pkill'.

2. write pidwait.sh
  > Done!

### Tmux

1. (skipped)

### Aliases

1. `alias dc='cd'

2. `$ alias thetoptenmostusedcommandsforthissession="history | awk '{\$1=\"\";print substr(\$0,2)}' | sort | uniq -c | sort -n | tail -n 10"`

3. (skipped)

### ssh

(later)

...
