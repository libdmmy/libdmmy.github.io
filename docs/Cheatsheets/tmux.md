# tmux

## commands
create a new session:
```bash
tmux new
```
add `-s your_session_name` if you want to set name of session  

Get in that session:
```bash
tmux at
```
add `-t your_session_name` if you specified name of session  

## useful keybindings (default)
`Ctrl+B c` - create a new window  
`Ctrl+B d` - detach from session, it'll keep running in the background  
`Ctrl+B ?` - display available keybindings  
`Ctrl+B n` - switch to the next window  
`Ctrl+B p` - switch to the previous window  
`Ctrl+B &` - kill current window  
