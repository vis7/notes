class EvalExpression():
    def __init__(self, n):
        self.ans = n

    @classmethod
    def equation1(cls, args):
        obj = cls((args[0]*args[0]) - (args[1]*args[1]))
        return obj

    @classmethod
    def equation2(cls, args):
        obj = cls((args[0]*args[0]) + (args[1]*args[1]) - args[2])
        return obj

    @classmethod
    def equation3(cls, args):
        sum = 0
        for i in args:
            sum += (i*i)

        obj = cls(sum/max(args))
        return obj


eq_ob = EvalExpression.equation1([1,2])
print(eq_ob.ans)

eq_ob = EvalExpression.equation2([1,2,3])
print(eq_ob.ans)

eq_ob = EvalExpression.equation3([1,2,3,4,5])
print(eq_ob.ans)
