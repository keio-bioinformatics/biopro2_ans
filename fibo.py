def fib(n):
    """nまでのフィボナッチ数列をリストとして返す関数"""
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series[:n]
