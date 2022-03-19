from mediantor import MediantorSqrtDecomp


if __name__ == "__main__":
    n: int = int(input())

    mediantor = MediantorSqrtDecomp(n)

    for _ in range(n):
        numbers: list[int] = list(map(int, input().split()))
        operation: int = numbers[0]
        if operation == 1:
            x: int = numbers[1]
            mediantor.insert(x)
        else:
            print(mediantor.take())
