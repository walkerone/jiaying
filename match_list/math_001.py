import random

for i in range( 1 ):
    m1 = random.randint( 4, 9 )
    n1 = random.randint( 4, 9 )
    q1 = n1 - 1
    sum = m1 * n1 + q1
    a = "(  )÷{}={}.....{}".format( str( m1 ), str( n1 ), str( q1 ) )
    # ---------------
    m2 = random.randint( 4, 9 )
    n2 = random.randint( 4, 9 )
    q2 = n2 - 1
    sum = m2 * n2 + q2
    b = "{}÷(  )={}.....{}".format( str( sum ), str( n2 ), str( q2 ) )
    # ---------------
    m3 = random.randint( 4, 9 )
    n3 = random.randint( 4, 9 )
    q3 = n2 - 1
    sum = m3 * n3 + q3
    c = "{}÷{}=(  ).....{}".format( str( sum ), str( m3 ), str( q3 ) )

    # ---------------
    m5 = random.randint( 90, 120 )
    n5 = random.randint( 90, 120 )
    q5 = random.randint( 90, 120 )
    sum = m5 + n5 - q5
    e = "{}+(  )-{}={}".format( str( m5 ), str( n5 ), str( q5 ), str( sum ) )

    print( a )
    print( b )
    print( c )
    print( e )
    # ---------------
    # 测试先括号再乘除，再加减
    m6 = random.randint( 90, 120 )
    n6 = random.randint( 90, 120 )
    s6 = random.randint( 5, 9 )
    h6 = random.randint( s6 - random.randint( 1, 4 ), s6 - 1 )
    k6 = random.randint( 30, 100 )
    sum = m6 + s6 * (s6 - h6) - k6
    f = "{}+ {}X({}-{})-{}={}".format( str( m6 ), str( s6 ), str( s6 ), str( h6 ), str( k6 ), str( sum ) )
    print( f )
    # ---------------
