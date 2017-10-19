#This test will pass
# def test_passing():
#   assert(1,2,3) == (1,2,3)

def add(x,y):
    return x + y

def test():
    assert add(2,3) == 4


#This Test Will fail
# def test_failing():
#     assert(1,2,3) == (3,2,1)