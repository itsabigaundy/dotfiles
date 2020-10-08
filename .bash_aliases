SRC=/mnt/c/Users/swima/source/
OMSCS=/mnt/c/Users/swima/source/OMSCS

cd $SRC
export DISPLAY=$(grep -m 1 nameserver /etc/resolv.conf | awk '{print $2}'):0.0

alias gcane="git commit --amend --no-edit"
alias gs="git status"

alias vimbashrc="vim ~/.bashrc"
alias srcbashrc="source ~/.bashrc"
alias vimaliases="vim ~/.bash_aliases"
alias vimvimrc="vim ~/.vimrc"
alias vimgitconfig="vim ~/.gitconfig"
