from kerykeion import KrInstance
import datetime
from colored import fg, bg, attr

current_time = datetime.datetime.now()

astro = KrInstance(
  "Now", 
  year=current_time.year,
  month=current_time.month,
  day=current_time.day,
  hour=current_time.hour,
  minute=current_time.minute,
  lat=37.8,
  lng=-122.4,
  tz_str="America/Los_Angeles",
  online=False
)

# dashboard!
sign_symbols = [
  "♈︎", "♉", "♊", "♋", "♌", "♍", "♎", "♏", "♐", "♑", "♒", "♓"
]
sign_abbreviations = [
  "Ari", "Tau", "Gem", "Can", "Leo", "Vir", "Lib", "Sco", "Sag", "Cap", "Aqu", "Pis"
]

tuple_table = [
  ("☉", astro.sun.sign_num, astro.sun.retrograde),
  ("☽", astro.moon.sign_num, astro.moon.retrograde),
  "spacer",
  ("☿", astro.mercury.sign_num, astro.mercury.retrograde),
  ("♀", astro.venus.sign_num, astro.venus.retrograde),
  ("♂", astro.mars.sign_num, astro.mars.retrograde),
  ("♃", astro.jupiter.sign_num, astro.jupiter.retrograde),
  ("♄", astro.saturn.sign_num, astro.saturn.retrograde),
  ("⛢", astro.uranus.sign_num, astro.uranus.retrograde),
  ("♆", astro.neptune.sign_num, astro.neptune.retrograde),
  ("♇", astro.pluto.sign_num, astro.pluto.retrograde),
]


line_one = ""
line_two = ""
for t in tuple_table:
  if t == "spacer":
    line_one += f"{attr(2)} {attr(0)}"
    line_two += f"{attr(2)} {attr(0)}"
  else: 
    if t[2]:
      foreground = fg(1)
      background = bg(0)
    else:
      foreground = fg(2)
      background = bg(0)
    line_one += f"{foreground}{background} {t[0]} {attr(0)}"
    line_two += f"{attr(2)}{fg(15)}{bg(0)}{sign_abbreviations[t[1]]}{attr(0)}"
  line_one += " "
  line_two += " "

table = f"{line_one}\n{line_two}"

def leftpad_multiline(string, padding):
  return "\n".join([padding + line for line in string.split("\n")])
table = leftpad_multiline(table, "  ")

print()
print(table)
print()
