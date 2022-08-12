import random

def match_001():
    m1 = random.randint(4, 10)
    n1 = random.randint(3, random.randint(3, m1))
    q1 = n1 - 1
    sum = m1 * n1 + q1
    a = "(  )÷{}={}.....{}".format(str(m1), str(n1), str(q1))
    print(a)

def match_002():
    m2 = random.randint(4, 10)
    n2 = random.randint(3, random.randint(3, m2))
    q2 = n2 - 1
    sum = m2 * n2 + q2
    b = "{}÷(  )={}.....{}".format(str(sum), str(n2), str(q2))
    print(b)

def match_003():
    m3 = random.randint(4, 10)
    n3 = random.randint(3, random.randint(3, m3))
    q3 = n3 - 1
    sum = m3 * n3 + q3
    c = "{}÷{}=(  ).....{}".format(str(sum), str(m3), str(q3))
    print(c)

def match_004():
    m5 = random.randint(90, 120)
    n5 = random.randint(90, 120)
    q5 = random.randint(90, 120)
    sum = m5 + n5 - q5
    e = "{}+(  )-{}={}".format(str(m5), str(n5), str(q5), str(sum))
    print(e)

def match_005():
    m6 = random.randint(90, 120)
    n6 = random.randint(90, 120)
    s6 = random.randint(5, 9)
    h6 = random.randint(s6 - random.randint(1, 4), s6 - 1)
    k6 = random.randint(30, 100)
    sum = m6 + s6 * (s6 - h6) - k6
    f = "{}+ {}X({}-{})-( )={}".format(str(m6), str(s6), str(s6), str(h6), str(sum))
    print(f)

def match_006():
    m7 = random.randint(12, 30)
    n7 = random.randint(5, 9)
    sum = m7 * n7

    h = "{}÷{}=(  )".format(str(sum), str(n7), )
    print(h)

def match_007():
    m7 = random.randint(5, 9)
    n7 = random.randint(10, 20)
    sum = m7 * n7

    h = "{} X {}=(  )".format(m7, str(n7), )
    print(h)


def match_008():
    m = random.randint(80, 99)
    n = random.randint(10, 20)
    h= random.randint(10, 20)

    h = "{} +{}- ( )={} - {}+ {}".format(str(h), str(m),str(m), str(n),str(h), )
    print(h)

def match_009():
    m7 = random.randint(10, 20)
    n7 = random.randint(10, 20)
    sum = m7 * n7

    h = "{} X {}=(  )".format(m7, str(n7), )
    print(h)

def match_010():
    m = random.randint(100, 300)
    n = random.randint(100, 300)
    q= random.randint(600, 650)

    result = "{}-( )={}+{}".format(str(q),str(m),str(n) )
    print(result)


for i in range(1):
    match_001()
    # ---------------
    match_002()
    # ---------------
    # match_003()

    # match_004()
    # match_005()

    match_006()
    match_007()
    match_008()
    # match_009()
    match_010()

# with open("unit.py","r+",encoding="utf-8") as file1:
#     with open("unit.py","w+",encoding="utf-8") as file2:
#         for line in file1:
#             if len(line.strip())==0:
#                 continue
#             else:
#                 file2.write(line
#                             )
