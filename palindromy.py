def palindrome(word):
  """Funkcja służy do sprawdzenia, czy dany wyraz jest palindromem. Palindrom słowo, które czytane od lewej do prawej i od prawej do lewej brzmi tak samo. Przykłady to “kajak” i “potop”.
  Argument:
  word: sprawdzany wyraz.
  Returns:
  True, jeśli tekst jest palindromem, False jeśli nie.
  """
  word = word.lower() 
  return word == word[::-1]  
print(palindrome("koza"))
print(palindrome("sedes"))
print(palindrome("kajak"))
print(palindrome("bąk"))
