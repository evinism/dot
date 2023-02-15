function moonphase(){
  python3 $DOTFILES_DIR/py/moonphase.py
}

function get_hostcolor(){
  # return a random color based on hostname
  # colors: blue, green, yellow,
  colors=("cyan" "magenta" "yellow" "orange")
  hostname=$(hostname)
  hash=$(echo $hostname | md5sum)
  index=$(( 16#${hash:0:2} % ${#colors[@]} ))
  echo ${colors[$index]}
}

hostcolor=$(get_hostcolor)

PROMPT=" %(?:%{$fg_bold[green]%}$(moonphase) :%{$fg_bold[red]%}$(moonphase) )"
PROMPT+=' %{$fg[$hostcolor]%}%c%{$reset_color%} $(git_prompt_info)'

ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg_bold[blue]%}(%{$fg[red]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%} "
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg[blue]%}) %{$fg[yellow]%}✗"
ZSH_THEME_GIT_PROMPT_CLEAN="%{$fg[blue]%})"
