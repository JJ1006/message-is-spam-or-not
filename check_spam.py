
text=input("Please enter the text : \n")
spam = False

if("make money easily" in text):
    spam = True
elif("but now pay later" in text):
    spam = True
elif("get instant money" in text):
    spam = True
else:
    spam = False

if(spam):
    print("\n\nCAUTION , The text is SPAM.\n\n")
else:
    print("\n\nThe text is NOT SPAM.\n\n")