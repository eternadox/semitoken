import datetime
import math
import base64
EPOCH = 1420070400000

# made by eternadox, github.com/eternadox :)

id = int(input("Enter ID for the funny: "))

timestamp = ((id >> 22) + EPOCH) / 1000
ts = math.floor(timestamp) 
middle = base64.b64encode(int(ts).to_bytes((ts.bit_length() + 7) // 8, 'big')).decode("utf-8").split("==")[0]
sample_string = str(id)
sample_string_bytes = sample_string.encode("ascii")
  
base64_bytes = base64.b64encode(sample_string_bytes)
first = base64_bytes.decode("ascii")
print("Encoded ID: "+first)
print("Timestamp of account creation (encoded): "+middle)
print(f"the funny semi-token: {first}.{middle}")

date= datetime.datetime.fromtimestamp(ts, tz=datetime.timezone.utc) # ignore this
