# Dec 1
num = int(input("Choose your number "))
print("Okay now, we are gonna do a binary search")
beg = 0  # give your start
end = 100  # give your end
while beg <= end:  # applied binary search algorithm
    find = (beg + end) // 2
    if find > num:
        msg = "you're too high!"
        end = find
    elif find < num:
        msg = "you're too low!"
        beg = find
    else:
        msg = "spot on!"
        print(f"Guess {find} (half of {beg} to {end}) -> {msg}")
        break
    print(f"Guess {find} (half of {beg} to {end}) -> {msg}")

# SAMPLE I/O
# Choose your number 38
# Okay now, we are gonna do a binary search
# Guess 50 (half of 0 to 50) -> you're too high!
# Guess 25 (half of 25 to 50) -> you're too low!
# Guess 37 (half of 37 to 50) -> you're too low!
# Guess 43 (half of 37 to 43) -> you're too high!
# Guess 40 (half of 37 to 40) -> you're too high!
# Guess 38 (half of 37 to 40) -> spot on!
