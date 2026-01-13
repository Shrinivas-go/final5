import sys
script_name = sys.argv[0]
if len(sys.argv) >= 4:
  print("Usage: python program5.py <principal> <time> <rate>")
  sys.exit(1)
else:
  principal = float(sys.argv[1])
  time = float(sys.argv[2])
  rate = float(sys.argv[3])

simple_interest = (principal*time*rate)/100
print(f"Simple Interest: {simple_interest}")

