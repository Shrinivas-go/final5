import sys

if len(sys.argv) == 4:
  script_name = float(sys.argv[0])
  principal = float(sys.argv[1])
  time = float(sys.argv[2])
  rate = float(sys.argv[3])
else:
  principal = 10000
  time = 2
  rate = 5.22

simple_interest = (principal*time*rate)/100
print(f"Simple Interest: {simple_interest}")

