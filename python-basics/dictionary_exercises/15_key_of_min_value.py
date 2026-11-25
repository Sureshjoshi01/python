# Write a code to print the key of a minimum value from the following dictionary.

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

min = sample_dict['Physics']
for k in sample_dict:
    if sample_dict[k] < min:
        min = sample_dict[k]

print(min)