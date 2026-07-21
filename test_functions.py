# Task 1 - easy number check
def test_number_is_10():
    number = 10
    assert number == 10 # should pass

# Task 2 - easy string check
def test_word_is_shruti():
    word = "shruti"
    assert word == "shruti" # should pass

# Task 3 - easy true -false check
def test_sky_is_blue():
    is_blue = True
    assert is_blue == False # should fail

# Practice example
username = "shruti@test123"
password = "Password@123"
def check_login(username, password):
    if "@" in username and len(password) >= 8:
        return True
    return False

def test_valid_login():
    assert check_login("shruti@test.com", "Password@123") == True

def test_invalid_email():
    assert check_login("shrutitest.com", "Password@123") == False

def test_weak_password():
    assert check_login("shruti@test.com", "Pass") == False

print(test_valid_login())
print(test_invalid_email())
print(test_weak_password())