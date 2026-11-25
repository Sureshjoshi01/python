# Remove empty strings from a list of strings


def rmv_empt_str(str_list):
    for i in str_list:
        if i == '' or i == None:
            str_list.remove(i)
    print(str_list)
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
rmv_empt_str(str_list)


