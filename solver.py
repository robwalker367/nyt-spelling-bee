
def construct_trie():
  root = dict()
  with open("scrabble-dictionary.txt", "r") as f:
    words = f.read().splitlines()
    for word in words:
      current_dict = root
      for letter in word:
        current_dict = current_dict.setdefault(letter.lower(), {})
      current_dict["end"] = word.lower()
  return root

print("NYT Spelling Bee Solver (11/21/2020) -- Rob Walker")
print("Please wait. Initializing dictionary...", end='', flush=True)

trie = construct_trie()

print(" done!")

mandatory_letter = input("Mandatory letter: ").lower()
print("You entered the mandatory letter: " + mandatory_letter.lower())

print("Please enter the other letters.")
letters = []
i = 1
while i < 7:
  x = input("Letter " + str(i) + ": ")
  if x in letters:
    print("You've already entered this letter!")
  elif not x.isalpha():
    print("Please enter a letter.")
  else:
    letters.append(x.lower())
    i += 1
print("You entered the non-mandatory letters: " + ", ".join(letters))

print("Finding words... ", end='', flush=True)

letters.append(mandatory_letter)
letters = sorted(letters)

found_words = []
def find_words(current_dict):
  if "end" in current_dict.keys() and mandatory_letter in current_dict["end"]:
    found_words.append(current_dict["end"])
  for letter in letters:
    if letter in current_dict.keys():
      find_words(current_dict[letter])

find_words(trie)

print("done!")

print("Found the following words:")
for word in found_words:
  print(word)
