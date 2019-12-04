
def validate_ssn(ssn):
    """Checks if the ssn is valid. Returns an error message if it is not"""
    if type(ssn) == int and len(str(ssn)) == 10:
        print("mammma")
    else:
        print("{} is invalid".format(ssn))


ssn = 2609003230
validate_ssn(ssn)