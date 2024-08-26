hold_lamda=lambda x:x*x
print(hold_lamda(2))

def myLambdaFunctionCheck(function_varirable):
    return (lambda lambda_variable:print(f"lambda_variable is {lambda_variable} and "
                                         "function_varirable is {function_varirable}"))
x=myLambdaFunctionCheck(10)
x(20)