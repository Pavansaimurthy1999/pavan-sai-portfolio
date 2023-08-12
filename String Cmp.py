from difflib import SequenceMatcher
def similar(str1, str2):
       return SequenceMatcher(None, str1, str2).ratio()
str1 = "HALLMARK GLOBAL TECHNOLOGIES"
str2 = "Hallmark Global Technologies"
res = similar(str1, str2)
print ("The similarity between 2 strings is : " + str(res))
