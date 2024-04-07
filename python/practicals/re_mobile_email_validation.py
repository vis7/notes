import re

# email validator
pattern = "^[a-zA-Z._%+-]+@[a-zA-Z.-]+.[a-zA-Z]{2,}$"
email = "vishvajeet@gmail.com"

result = re.match(pattern, email)

if result:
    print("match successful")
else:
    print("match failed")

# mobile validation (only number not phone code)
pattern = "[9876]\d{9}"
mobile = "9300676751"

result = re.match(pattern, mobile)

if result:
    print("match successful")
else:
    print("match failed")

