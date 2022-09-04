import random


def match_001():
    m = random.randint( 100, 500 )
    n = random.randint( 3, 7 )

    m1 = random.randint( 200, 400 )
    n1 = random.randint( 3, 7 )

    m2 = random.randint( 100, 300 )
    n2 = random.randint( 3, 7 )
    print( '{}X{} + {}X{} - {}X{}=( )'.format( str( m ), str( n ), str( m1 ), str( n1 ), str( m2 ), str( n2 ) ) )

    m = random.randint( 100, 500 )
    n = random.randint( 3, 7 )

    m1 = random.randint( 200, 400 )
    n1 = random.randint( 3, 7 )

    m2 = random.randint( 100, 300 )
    n2 = random.randint( 3, 7 )
    print( '{}X{} - {}X{} + {}X{}=( )'.format( str( m ), str( n ), str( m1 ), str( n1 ), str( m2 ), str( n2 ) ) )


def match_002():
    m = random.randint( 200, 600 )
    n = random.randint( 4, 9 )

    if "0" not in str( m ):
        print( '{} X {}  =( )'.format( str( m ), str( n ), ) )


def match_003():
    m = random.randint( 30, 100 )
    n = random.randint( 4, 10 )
    sum = m * n
    data = '{} ÷ {} =( )'.format( str( sum ), str( n ) )
    if "0" not in str( data ):
        print( data )


def match_004():
    m = random.randint( 1000, 5000 )
    n = random.randint( 1000, 5000 )
    data = '{} + {} =( )'.format( str( m ), str( n ) )
    print( data )


for i in range( 3 ):
    match_002()
    match_003()
    match_004()
