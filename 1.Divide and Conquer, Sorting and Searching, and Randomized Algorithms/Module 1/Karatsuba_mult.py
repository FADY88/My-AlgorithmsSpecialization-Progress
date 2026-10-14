# Grade-School Algorithm for Multiplying
def KaratsubaMult(x, y):
  pos = False
  if (x < 0) == (y < 0): pos = True
  x = abs(x)
  y = abs(y)
  # base case
  if x < 10 and y < 10:
    return x * y if pos else -(x * y)
  
  x = str(x)
  y = str(y)
  # recursive case
  # x * y = 10**n ac + 10**n/2 (ad + bc) + bd
  n = len(x)
  m = len(y)
  # organizing input

  while n != m or n % 2 == 1:
    if n > m:
      y = "0" + y
      m += 1
    elif m > n:
      x = "0" + x
      n += 1
    else:
      x = "0" + x
      n += 1
      y = "0" + y
      m += 1
  a = int(x[0:n//2])
  b = int(x[n//2:n])
  c = int(y[0:n//2])
  d = int(y[n//2:n])
  #recursion and padding step
  # 10**n ac
  ac = KaratsubaMult(a, c)
  bd = KaratsubaMult(b, d)
  step3 = KaratsubaMult(a + b, c + d)
  # 10**n/2 (ad + bc)
  ad_bc = int(str(step3 - bd - ac) + "0" * (n//2))
  ac = int(str(ac) + "0" * n)
  
  result = ac + ad_bc + bd
  return result if pos else -result


# Test cases
def test_multiply():
    # Positive numbers
    assert KaratsubaMult(2, 3) == 6, "Failed on positive numbers"
    assert KaratsubaMult(10, 5) == 50, "Failed on positive numbers"
    assert KaratsubaMult(123456, 654321) == 80779853376, "Failed on large positive numbers"

    # Negative numbers
    assert KaratsubaMult(-2, 3) == -6, "Failed on negative numbers"
    assert KaratsubaMult(-4, -5) == 20, "Failed on negative numbers"
    assert KaratsubaMult(-123456, -654321) == 80779853376, "Failed on large negative numbers"

    # Mixed sign numbers
    assert KaratsubaMult(7, -3) == -21, "Failed on mixed sign numbers"
    assert KaratsubaMult(-6, 4) == -24, "Failed on mixed sign numbers"
    assert KaratsubaMult(987654, -123456) == -121931812224, "Failed on large mixed sign numbers"

    # Zero
    assert KaratsubaMult(0, 5) == 0, "Failed on zero"
    assert KaratsubaMult(3, 0) == 0, "Failed on zero"
    assert KaratsubaMult(0, 0) == 0, "Failed on zero"

    # Very large numbers
    assert KaratsubaMult(10**6, 10**6) == 10**12, "Failed on very large numbers"
    assert KaratsubaMult(-10**6, 10**6) == -10**12, "Failed on very large numbers with mixed signs"
    assert KaratsubaMult(10**12, 10**12) == 10**24, "Failed on extremely large numbers"

    # main test
    assert KaratsubaMult(5963, 4128) == 24615264, "Failed on big number"
    assert KaratsubaMult(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627) == 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184, "Failed on main test"


# Run tests
# print(KaratsubaMult(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))
test_multiply()
print("All tests passed!")