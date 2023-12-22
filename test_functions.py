from functions import salary,hello_who,privet_who


def test_hello_who_max():
    assert hello_who('Max') =='Hello,Max'
def test_hello_who_max():
    assert hello_who('sigma') =='Hello,sigma'

def test_privet_who_sigma():
    assert privet_who('sigma') =='privet,sigma'

def test_salary():
    assert salary(2, 2) == 8
    assert salary(3, 1) ==6
