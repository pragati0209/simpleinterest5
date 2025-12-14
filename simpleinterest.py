import sys

# Check if command-line arguments are given
if len(sys.argv) == 4:
    script_name = sys.argv[0]
    p = float(sys.argv[1])
    r = float(sys.argv[2])
    t = float(sys.argv[3])
else:
    script_name = sys.argv[0]
    p = 10000
    r = 10
    t = 2
    print("No input given – using default values")

# Calculate Simple Interest
si = (p * r * t) / 100

print("Script Name:", script_name)
print("Principal Amount:", p)
print("Rate of Interest:", r)
print("Time:", t)
print("Simple Interest:", si)
