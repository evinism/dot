# Calculate Lunar Phase
# Author: Sean B. Palmer, inamidst.com
# Cf. http://en.wikipedia.org/wiki/Lunar_phase#Lunar_phase_calculation

get_moon_position() {
    if [ -z "$1" ]; then
        now=$($DATE_CMD +'%s')
    else
        now=$($DATE_CMD -d "$1" +'%s')
    fi

    diff=$((now - $($DATE_CMD -d '2001-01-01' +'%s')))
    days=$(echo "scale=10; $diff / 86400" | bc)
    lunations=$(echo "scale=10; 0.20439731 + $days * 0.03386319269" | bc)

    echo "$lunations % 1" | bc
}

if ! command -v gdate &> /dev/null
then
    DATE_CMD=date 
else
    DATE_CMD=gdate
fi

get_moon_phase() {
    pos=$1
    waxing_waning=$(echo "$pos < 0.5" | bc -l)
    if (( $(echo "0.485 < $pos && $pos < 0.515" | bc -l) )); then
        icon=$'\u2600'
    else
        index=$(echo "scale=0; $pos * 8 + 0.5" | bc)
        icon=$(
            case $(($index & 7)) in
                0) echo $'\u25cb';;
                1) echo $'\u25d4';;
                2) echo $'\u25d1';;
                3) echo $'\u25d5';;
                4) echo $'\u25cf';;
                5) echo $'\u25d5';;
                6) echo $'\u25d1';;
                7) echo $'\u25d4';;
            esac
        )
    fi
    waxing_indicator=$'\u0307'
    waning_indicator=$'\u0323'
    #if [ -z "$DISABLE_WAXING_WANING" ]; then
      if [[ $waxing_waning -eq 1 ]]; then
        echo "${icon}${waxing_indicator}"
      else
        echo "${icon}${waning_indicator}"
      fi
    #else
    #  echo $icon
    #fi
}

moonphase() {
  pos=$(get_moon_position "$1")
  phasename=$(get_moon_phase $pos)
  echo "$phasename"
}

function get_hostcolor(){
  # return a random color based on hostname
  # colors: blue, green, yellow,
  colors=(
    "cyan"
    "magenta"
    "yellow"
    "orange"
    "white"
    "blue",
    "green"
  )
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
