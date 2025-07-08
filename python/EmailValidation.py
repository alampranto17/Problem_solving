
def ValidEmail(email):

    invalid_characters = "1234567890.+-_ @"

    if email[0] in  invalid_characters or email[-1] in  invalid_characters:
        return False

    if(email.count("@")!=1 or email.count(".")!=1):
        return False

    list=email.split(".",1)


    if(list[-1]!="com"):
        return False


    return True;







email=input("Enter a Email: ")


if(ValidEmail(email)):
    print("Valid email ")
else:
    print("Invalid Email")



