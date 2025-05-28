
text = input("Input: ").strip()
vowels = "aeiouAEIOU"
novowel = "".join(c for c in text if c not in vowels)
print(novowel)
