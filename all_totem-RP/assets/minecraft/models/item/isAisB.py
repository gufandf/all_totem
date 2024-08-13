def isAisB(A,B):
    if len(A) >= len(B):
        if A[0:len(B)] == B and len(A) - len(B) <8:
            return True
        else:
            return False
    else:
        return isAisB(B,A)
