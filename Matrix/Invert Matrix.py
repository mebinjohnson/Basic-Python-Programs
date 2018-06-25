import copy
from fractions import Fraction

def makeIdentity(n):
    result = make2dList(n,n)
    for i in xrange(n):
        result[i][i] = Fraction(1, 1)
    return result



def multiplyMatrices(a, b):
    # confirm dimensions
    aRows = len(a)
    aCols = len(a[0])
    bRows = len(b)
    bCols = len(b[0])
    assert(aCols == bRows) # belongs in a contract 
    rows = aRows
    cols = bCols
    # create the result matrix c = a*b
    c = make2dList(rows, cols)
    # now find each value in turn in the result matrix
    for row in xrange(rows):
        for col in xrange(cols):
            dotProduct = Fraction(0, 1)
            for i in xrange(aCols):
                dotProduct += a[row][i]*b[i][col]
            c[row][col] = dotProduct
    return c


def multiplyRowOfSquareMatrix(m, row, k):
    n = len(m)
    rowOperator = makeIdentity(n)
    rowOperator[row][row] = k
    return multiplyMatrices(rowOperator, m)

def addMultipleOfRowOfSquareMatrix(m, sourceRow, k, targetRow):
    # add k * sourceRow to targetRow of matrix m
    n = len(m)
    rowOperator = makeIdentity(n)
    rowOperator[targetRow][sourceRow] = k
    return multiplyMatrices(rowOperator, m)


def invertMatrix(m):
    n = len(m)
    assert(len(m) == len(m[0]))
    inverse = makeIdentity(n) # this will BECOME the inverse eventually
    for col in xrange(n):
        # 1. make the diagonal contain a 1
        diagonalRow = col
        assert(m[diagonalRow][col] != 0) # @TODO: actually, we could swap rows
                                         # here, or if no other row has a 0 in
                                         # this column, then we have a singular
                                         # (non-invertible) matrix.  Let's not
                                         # worry about that for now.  :-)
        k = Fraction(1,m[diagonalRow][col])
        m = multiplyRowOfSquareMatrix(m, diagonalRow, k)
        inverse = multiplyRowOfSquareMatrix(inverse, diagonalRow, k)
        # 2. use the 1 on the diagonal to make everything else
        #    in this column a 0
        sourceRow = diagonalRow
        for targetRow in xrange(n):
            if (sourceRow != targetRow):
                k = -m[targetRow][col]
                m = addMultipleOfRowOfSquareMatrix(m, sourceRow, k, targetRow)
                inverse = addMultipleOfRowOfSquareMatrix(inverse, sourceRow,
                                                         k, targetRow)
    # that's it!
    return inverse


def make2dList(rows, cols):
    a=[]
    for row in xrange(rows): a += [[0]*cols]
    return a
    
def printMatrix(a):
    def valueStr(value):
        if (isinstance(value, Fraction)):
            (num, den) = (value.numerator, value.denominator)
            if ((num == 0) or (den == 1)): return str(num)
            else: return str(num) + "/" + str(den)
        else:
            return str(value)
    def maxItemLength(a):
        maxLen = 0
        rows = len(a)
        cols = len(a[0])
        for row in xrange(rows):
            for col in xrange(cols):
                maxLen = max(maxLen, len(valueStr(a[row][col])))
        return maxLen
    if (a == []):
        # So we don't crash accessing a[0]
        print []
        return
    rows = len(a)
    cols = len(a[0])
    fieldWidth = maxItemLength(a)
    print "[",
    for row in xrange(rows):
        if (row > 0) and (len(a[row-1]) > 1): print "\n  ",
        print "[",
        for col in xrange(cols):
            if (col > 0): print ",",
            # The next 2 lines print a[row][col] with the given fieldWidth
            format = "%" + str(fieldWidth) + "s"
            print format % valueStr(a[row][col]),
        print "]",
    print "]"


a=[[1,-1,1],[2,1,-3],[1,1,1]]

a=[[2,-3,5],[3,2,-4],[1,1,-2]]
print a
b=invertMatrix(a)
printMatrix(b)
