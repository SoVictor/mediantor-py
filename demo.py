from mediantor import MediantorSortedList


if __name__ == "__main__":
    mediantor = MediantorSortedList()

    n: int = int(input())
    for _ in range(n):
        numbers: list[int] = list(map(int, input().split()))
        operation: int = numbers[0]
        if operation == 1:
            x: int = numbers[1]
            mediantor.insert(x)
        else:
            print(mediantor.take())
