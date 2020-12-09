def string_rot(s,l):
  return s[l::]+s[:l:]


def string_rot_cycle(s):
  tmp = []
  for i in range(0,len(s)):
    s = string_rot(s,1)
    tmp.append(s)
  return tmp

