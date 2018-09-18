# Example: a sample ~/.bash_profile file
# customize the prompt appearance
export PS1="\\u@\h \\W]\\$"
# add current directory to PATH
export PATH=.:$PATH
# avoid overwriting files with output redirection
set -o noclobber
# prompt user for removing or overwriting files with rm, cp, mv
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
# store most recent terminal commands in the file .bash_history
export HISTFILE=".bash_history"
# alias for printing last 10 commands
alias h='history | tail'
# alias ls and ll to use my favorite flags by default
alias ls='ls -Ft'
alias ll="ls -Fthalr";
