# Implement binary search

def binary_search(array, item)
  if array.length == 0
    return false
  else
    midpoint = array.length/2
    if array[midpoint] == item
      return true
    elsif array[midpoint] > item
      return binary_search(array[0...midpoint], item)
    else
      return binary_search(array[midpoint+1..-1], item)
    end
  end
end

test_array = [1,4,6,7,10,12,16,19,40,41,51,70,81,99,100]
puts binary_search(test_array, 16)
puts binary_search(test_array, 18)
puts binary_search([1,9], 9)
puts binary_search([], 9)
puts binary_search([1,2,3], 2)
puts binary_search([1,2,4], 3)
