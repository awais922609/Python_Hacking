import sys


def caesar_cipher_converter(message, key, mode):
  letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  translated = ''
  message = message.upper()
  key = key % 26  # Ensures the key is within 0-25

  for char in message:
    if char in letters:
      temp_index = letters.find(char)
      if mode == 'encrypt':
        temp_index = (temp_index + key) % 26
      elif mode == 'decrypt':
        temp_index = (temp_index - key) % 26
      else:
        raise ValueError("Mode should be 'encrypt' or 'decrypt'")
      translated += letters[temp_index]
    else:
      # Preserve non-alphabet characters
      translated += char

  return translated


def main():
  # Check if the correct number of arguments is provided
  if len(sys.argv) != 4:
    print("Usage: python script_name.py <message> <key> <mode>")
    print("Example: python script_name.py 'Hello World' 3 encrypt")
    sys.exit(1)

  # Assign command-line arguments to variables
  message = sys.argv[1]

  try:
    key = int(sys.argv[2])
  except ValueError:
    print("Key must be an integer.")
    sys.exit(1)

  mode = sys.argv[3].lower()

  try:
    result = caesar_cipher_converter(message, key, mode)
    print(f"Result: {result}")
  except ValueError as ve:
    print(ve)
    sys.exit(1)


if __name__ == "__main__":
  main()
