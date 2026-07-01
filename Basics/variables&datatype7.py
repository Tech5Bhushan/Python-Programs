#Predict the output: t = (1, 2, 3)   t[0] = 99   print(t) — will this run? Why or why not?
#ANSWER : N0, program will NOT Run, since the 'tuple' type is immutable. The t[0] will NOT get replaced with 99 and program will through a Type error.
# Actual error will be "TypeError: 'tuple' object does not support item assignment"

t = (1,2,3)
t[0] = 99
print(t)