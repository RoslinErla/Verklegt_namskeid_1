
def validate_ssn(ssn):
    """Checks if the ssn is valid. Returns an error message if it is not"""
    if type(ssn) == int and len(str(ssn)) == 10:
        print("mammma")
    else:
        print("{} is invalid".format(ssn))

def validate_phone_number(phone_number):
    if type(phone_number) == int and len(str(phone_number)) == 7:
        print("mamma")
    else:
        print("{} is invalid".format(phone_number))

def validate_rank(rank):
    if rank.lower() == "flight attendant" or rank.lower() == "flight service manager" \
        or rank.lower() == "co-pilot" or rank.lower() == "captain":
        print("mamma")
    else:
        print("GUÐJÓN")

rank = "Co-mom"
validate_rank(rank)