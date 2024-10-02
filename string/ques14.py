str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res_list = []
for x in str_list:
    # check for non empty string
    if x:
        res_list.append(x)
print(res_list)

