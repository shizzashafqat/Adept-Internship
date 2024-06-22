def xor(a, b):
  """Performs bitwise XOR between two binary strings"""
  result = ""
  for i in range(len(a)):
    if (a[i] == '1' and b[i] == '1') or (a[i] == '0' and b[i] == '0'):
      result += '0'
    else:
      result += '1'
  return result

def mod2div(dividend, divisor):
  """Performs Modulo-2 division of binary strings"""
  pick = len(divisor)
  tmp = dividend[:pick] if len(dividend) >= pick else dividend + "0" * (pick - len(dividend))
  n = len(dividend)

  while pick < n:
    if tmp[0] == '1':
      tmp = xor(divisor, tmp) + dividend[pick]
    else:
      pick = min(pick, len(tmp))  # Ensure pick doesn't exceed tmp length
      tmp = xor("0" * pick, tmp) + dividend[pick]
    pick += 1
    tmp = tmp[1:]

  if tmp[0] == '1':
    tmp = xor(divisor, tmp)
  else:
    pick = min(pick, len(tmp))  # Ensure pick doesn't exceed tmp length
    tmp = xor("0" * pick, tmp)

  return tmp[1:]


def encode_data(data, key):
  """Encodes data by appending the remainder"""
  appended_data = data + "0" * (len(key) - 1)
  remainder = mod2div(appended_data, key)
  encoded_data = data
  print("Encoded Data (Data):", encoded_data)  # Show only the data being sent

  # Print the remainder for informational purposes (not sent)
  print("Remainder:", remainder)

def receiver(data, key):
  """Checks received data for errors"""
  # Extract the actual data length from the received string
  data_len = len(data) - len(key) + 1  # Subtract key length and add 1 for potential padding
  remainder = mod2div(data[:data_len], key)  # Use extracted data length
  print("Final remainder at receiver:", remainder)
  if "1" in remainder:
    print("There is some error in the data")
  else:
    print("Correct message received")

def main():
  """Main function to drive the program"""
  data = input("Enter data (binary): ")
  key = input("Enter key (binary): ")

  print("Sender side...")
  encode_data(data, key)

  print("\nReceiver side...")
  encoded_data = data + mod2div(data + "0" * (len(key) - 1), key)
  receiver(encoded_data, key)

if __name__ == "__main__":
  main()
