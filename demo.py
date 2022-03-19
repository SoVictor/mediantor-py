from mediantor import IMediantor, Mediantor, make_mediantor


if __name__ == "__main__":
    mediantor_type: int = -1
    while mediantor_type < 0 or mediantor_type >= len(Mediantor):
        print("Please choose which Mediantor implementation to use by writing a single number:")
        print("0 - Mediantor as two heaps")
        print("1 - Mediantor as SQRT-decomposition")
        print("2 - Mediantor as a sorted list")
        mediantor_type = int(input())

    print("Please provide an input in a format described in README:")

    n: int = int(input())

    mediantor: IMediantor = make_mediantor(Mediantor(mediantor_type), n)

    ans: list[int] = list()
    for _ in range(n):
        numbers: list[int] = list(map(int, input().split()))
        operation: int = numbers[0]
        if operation == 1:
            x: int = numbers[1]
            mediantor.insert(x)
        else:
            ans.append(mediantor.take())

    print()
    print("Output:")
    for x in ans:
        print(x)
