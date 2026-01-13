import sys

if len(sys.argv) != 4:
    print("Usage: python simple_interest.py <principal> <rate> <time>")
    sys.exit(1)

principal = float(sys.argv[1])
time = float(sys.argv[2])
rate = float(sys.argv[3])

simple_interest = (principal * time * rate) / 100

print("Principal:", principal)
print("Time:", time)
print("Rate:", rate)
print("Simple Interest:", simple_interest)
