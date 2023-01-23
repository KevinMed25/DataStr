import array_stack as stack

def is_matched(expr):
  """Return True if all delimiters are properly match; False otherwise."""
  S = stack.ArrayStack()
  for c in expr:
    if c == '(':
      S.push(c)                               # push left delimiter on stack
    elif c == ')':
      if S.is_empty():
        return False
      S.pop()                     
  return S.is_empty()   

test = ['()(())()(()(())', ')(','(()()((())))','(()))']
for test_str in test:
  print(test_str)
  if is_matched(test_str):
    print('Paréntesis balanceados')
  else:
    print('Paréntesis no balanceados')

