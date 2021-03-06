#!/home/mwb33/.local/bin/pytest

# Name: Dinh Nguyen - CS 260 Summer 2020
# option -v to show individual test

#The Normal Python Function
def pow1(a,b):
	return a**b
#Computes a^b (integers a,b)
#Only works for b >= 0
def pow2(a,b):
	total=1
	for i in range(0,b):
		total=total*a
	return total
#Computes a^b (integers a,b)
#Only works for b >= 0
def pow3(a,b):
	if b==0:
		return 1
	elif b%2==1:
		return a*pow3(a,b-1)
	else:
		temp=pow3(a,b//2)
		return temp*temp

# ***** Begin test pow1 *****
def test_pow1_small_nums():
	a,b = 2, 3
	assert pow1(a,b)==8

	
def test_pow1_large_nums():
	a,b = 10000,2
	assert pow1(a,b)==100000000


def test_pow1_base_0():
	a,b = 0,121
	assert pow1(a,b)==0


def test_pow1_base_1():
	a,b = 1, 1000
	assert pow1(a,b)==1


def test_pow1_powerof_0():
	a,b = 5, 0
	assert pow1(a,b)==1

# ***** Begin test pow2 *****
def test_pow2_small_nums():
        a,b = 2, 3
        assert pow2(a,b)==8


def test_pow2_large_nums():
        a,b = 10000,2
        assert pow2(a,b)==100000000


def test_pow2_base_0():
        a,b = 0, 121
        assert pow2(a,b)==0


def test_pow2_base_1():
        a,b = 1, 1000
        assert pow2(a,b)==1


def test_pow2_powerof_0():
        a,b = 5, 0
        assert pow2(a,b)==1

# ***** Begin test pow3 *****
def test_pow3_small_nums():
        a,b = 2, 3
        assert pow3(a,b)==8


def test_pow3_large_nums():
        a,b = 10000,2
        assert pow3(a,b)==100000000


def test_pow3_base_0():
        a,b = 0,121
        assert pow3(a,b)==0


def test_pow3_base_1():
        a,b = 1, 1000
        assert pow3(a,b)==1


def test_pow3_powerof_0():
        a,b = 5, 0
        assert pow3(a,b)==1


# ****END****
