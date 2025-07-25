class BreakException(Exception):
    pass
try:
    for i in range(1,5):
        print("i:",i)
        for k in range(1,4):
            print("k:",k)
            if i == 3:
                raise BreakException
            print("End k:",k)
        print("End i:",i)    
        print("="*20)
except:
    pass

    
