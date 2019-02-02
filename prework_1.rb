# A pangram is a phrase which contains every letter at least once, such as
# “the quick brown fox jumps over the lazy dog”. Write a function which
# determines if a given string is a pangram.

# Strategy 1
# Go through every letter in the alphabet and check to see if it's in the string
# Time complexity: O(N)
# Space complexity: O(N)
def panagram1(str)
  str = str.downcase
  alphabet = ('a'..'z').to_a
  alphabet.each do |letter|
    return false unless str.include?(letter)
  end

  return true
end

# Strategy 2
# Work backwards to eliminate extra characters and check length
# Time complexity: O(N)
# Space complexity: O(N)
def panagram2(str)
  cleaned_string = str.downcase.delete("^a-z")
  unique_letters = cleaned_string.chars.uniq
  unique_letters.length == 26
end

# Strategy 3
# Make a list and check the length
# Time complexity: O(N)
# Space complexity: O(N)
def panagram3(str)
  cleaned_string = str.downcase.delete("^a-z")
  letters = {}
  cleaned_string.chars.each do |letter|
    letters[letter] = true
  end
  letters.keys.length == 26
end

puts panagram1('the quick brown fox jumps over the lazy dog')
