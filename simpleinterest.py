import sys

# Check whether correct number of arguments are passed or not
if len(sys.argv) != 4:
    print("Usage: python simple_interest.py <principal> <rate> <time>")
    sys.exit(1)

# Reading values from command line arguments
principal = float(sys.argv[1])
rate = float(sys.argv[2])
time = float(sys.argv[3])

# Calculate Simple Interest
simple_interest = (principal * rate * time) / 100

# Display result
print("Simple Interest is:", simple_interest)