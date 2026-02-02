num = int(input("Enter a number: "))
shift = int(input("Enter number of shift positions: "))

left_shift = num << shift
right_shift = num >> shift

print("Left Shift (", num, "<<", shift, ") =", left_shift)
print("Right Shift (", num, ">>", shift, ") =", right_shift)
