#Create a new string made of the first, middle, and last characters of each input string

def string_made_of_first_mid_last_of_input_string(s1,s2):
    s3 = s1[0] + s2[0]
    s4 = s1[int(len(s1)/2)] + s2[int(len(s2)/2)]
    s5 = s1[-1] + s2 [-1]
    final_str = s3+s4+s5
    print(final_str)

s1 = "America"
s2 = "Japan"
string_made_of_first_mid_last_of_input_string(s1,s2)
