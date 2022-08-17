import random
def match_001():
    m = random.randint(100,500)
    n= random.randint(3,7)

    m1 = random.randint(200, 400)
    n1 = random.randint(3, 7)

    m2 = random.randint(100, 300)
    n2 = random.randint(3, 7)
    print('{}X{} + {}X{} - {}X{}=( )'.format(str(m),str(n),str(m1),str(n1),str(m2),str(n2)))

    m = random.randint(100, 500)
    n = random.randint(3, 7)

    m1 = random.randint(200, 400)
    n1 = random.randint(3, 7)

    m2 = random.randint(100, 300)
    n2 = random.randint(3, 7)
    print('{}X{} - {}X{} + {}X{}=( )'.format(str(m), str(n), str(m1), str(n1), str(m2), str(n2)))

for i in range(5):
    match_001()