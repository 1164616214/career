# 阶乘
# n! = 1x2x3x...n

def fact(n):
    """
    1 定义的时候调用自己
    2 要有停止条件
    3 防止栈溢出，控制递归的次数
    应用：查看当前目录先的所有子目录及文件...
    """
    if n == 1:
        return 1
    return n * fact(n-1)
        

