print(r'''

                                          You shut up now!

                                        ,
         :                 .-,.-'')    /
         .                / / `  /
         .               (-'   .' \  _...__
                         \    / `> )'      `--.__
                          \ ,/     )         -._ `.
                         /  / _/  /             `.)
                         \_/L/ \_(.      .        `-.
                 _               \        \          `-
                 \`.            __\        |  .        `.
                  \\\        .--\  \:      J /    -.     .
         ._______  \\\      /  _.\ _J.-----.=-'           \
         \ ------`\ .-.    /./// .'        /\    _         L
          `-------_( (dP, ''')

print("welcome to the python pizza deliveries")

size = input("what size pizza do you want? S, M, or L")
size = size.upper()
pepperoni = input("Do you want peporoni on your pizza? Y or N")
pepperoni = pepperoni.upper()
extra_cheese = input("Do you want extra cheese? Y or N")
extra_cheese = extra_cheese.upper()
bill = 0
if size == "S":
    bill = 15

    if pepperoni == "Y":
        bill += 2

if size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3

if size == "L":
    bill = 25

    if pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"your final bill is {bill}")