# Grade-School Algorithm for Multiplying
def GradeSchoolMult(x, y):
  pos = False
  if (x < 0) == (y < 0): pos = True
  x = abs(x)
  y = abs(y)
  result = 0
  digit = 0
  padding = 1
  # I think the padding step can be improved by converting numbers
  # to string and append zeros to it
  while y > 0:
    digit = y % 10
    result += digitMult(x, digit) * padding
    y = y // 10
    padding *= 10
  return result if pos else -result

# digitMult using loops and lists
# def digitMult(x, digit):
#   digits = []
#   carry = 0
#   tmp = 0
#   while x > 0:
#     tmp = x % 10 * digit + carry
#     if tmp > 9:
#       digits.append((tmp) % 10)
#       carry = tmp // 10
#     else:
#       digits.append(tmp)
#       carry = 0
#     x //= 10

#   if carry > 0: digits.append(carry)
#   digits.reverse()
#   result = 0
#   for d in digits:
#     result *= 10
#     result += d
#   return result


# digitMult using Recursion
def digitMult(x, digit, carry = 0):
  # base case
  if x < 10:
    return x * digit + carry
  # get answer and add the carry
  tmp = x % 10 * digit + carry
  ans = tmp % 10
  if tmp > 9:
    carry = tmp // 10
  else:
    carry = 0

  return digitMult(x // 10, digit, carry) * 10 + ans



# Test cases
def test_multiply():
    # Positive numbers
    assert GradeSchoolMult(2, 3) == 6, "Failed on positive numbers"
    assert GradeSchoolMult(10, 5) == 50, "Failed on positive numbers"
    assert GradeSchoolMult(123456, 654321) == 80779853376, "Failed on large positive numbers"

    # Negative numbers
    assert GradeSchoolMult(-2, 3) == -6, "Failed on negative numbers"
    assert GradeSchoolMult(-4, -5) == 20, "Failed on negative numbers"
    assert GradeSchoolMult(-123456, -654321) == 80779853376, "Failed on large negative numbers"

    # Mixed sign numbers
    assert GradeSchoolMult(7, -3) == -21, "Failed on mixed sign numbers"
    assert GradeSchoolMult(-6, 4) == -24, "Failed on mixed sign numbers"
    assert GradeSchoolMult(987654, -123456) == -121931812224, "Failed on large mixed sign numbers"

    # Zero
    assert GradeSchoolMult(0, 5) == 0, "Failed on zero"
    assert GradeSchoolMult(3, 0) == 0, "Failed on zero"
    assert GradeSchoolMult(0, 0) == 0, "Failed on zero"

    # Very large numbers
    assert GradeSchoolMult(10**6, 10**6) == 10**12, "Failed on very large numbers"
    assert GradeSchoolMult(-10**6, 10**6) == -10**12, "Failed on very large numbers with mixed signs"
    assert GradeSchoolMult(10**12, 10**12) == 10**24, "Failed on extremely large numbers"

    # main test
    assert GradeSchoolMult(5963, 4128) == 24615264, "Failed on big number"
    assert GradeSchoolMult(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627) == 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184, "Failed on main test"


# Run tests
print(GradeSchoolMult(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))
test_multiply()
print("All tests passed!")