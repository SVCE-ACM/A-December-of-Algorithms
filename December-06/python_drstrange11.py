# Dec 6
# COntains optional too


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(arr, n):
    val = arr[0]
    for i in range(1, n):
        val = (arr[i]*val)//(gcd(arr[i], val))
    return val


# Enter the numbers with spaces
nums = list(map(int, input("Enter the numbers: ").split()))
nums.sort()
print(f"LCM: {lcm(nums,len(nums))}")

# SAMPLE I/O
# Enter the numbers: 12 7
# LCM: 84
