# Write a Python program to merge two dictionaries into one.

def merge_dicts(dict1, dict2):
    # Create a copy of dict1 to avoid modifying it directly
    merged_dict = dict1.copy()
    
    # Update the copy with the contents of dict2
    merged_dict.update(dict2)
    
    # Return the merged dictionary
    return merged_dict

# Example dictionaries
dict1 = {"name": "Azraa", "age": 18, "city": "Dubai"}
dict2 = {"university": "Bath Spa", "hobbies": ["Reading", "Painting"]}

# Merge dictionaries
merged_dict = merge_dicts(dict1, dict2)

# Print merged dictionary
print(merged_dict)