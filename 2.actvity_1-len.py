#len

# Tuple    
test_tuple = (1, 2, 3)
print('length of', test_tuple,'is', len(test_tuple))

# List    
test_list = [1, 2, 3]
print('length of', test_list,'is', len(test_list))

# Range    
test_range = range(1,10)
print('length of', test_range,'is', len(test_range))

# String
test_string = ""    
print('length of', test_string,'is', len(test_string))

test_string = "Python"    
print('length of', test_string,'is', len(test_string))

# Byte Object

test_string = b"Python"    
print('length of', test_string,'is', len(test_string))

test_list = [1, 2, 3]
test_byte = bytes(test_list)
print('length of', test_byte,'is', len(test_byte))


# Set

test_set = {1,2,3,4}
print('length of', test_set,'is', len(test_set))

test_set = set()
print('length of', test_set,'is', len(test_set))

# Dict

test_dict = {1:'one' , 2:'two' , 3:'three'}
print('length of', test_dict,'is', len(test_dict))

test_dict = {}
print('length of', test_dict,'is', len(test_dict))