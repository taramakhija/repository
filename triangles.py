import math
def triangle_3rd_side():
    a = int(input(" what does a equal"))
    b = int(input(" what does b equal"))
    csqr= a*2 + b*2
    c = math.sqrt(csqr)
    print(f"the third side is {c}")
triangle_3rd_side()