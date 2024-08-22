if __name__ == '__main__':
    N = int(input())  # Number of commands

    arr = []

    for _ in range(N):
        command = input().strip().split()
        action = command[0]

        if action == "insert":
            index = int(command[1])
            value = int(command[2])
            arr.insert(index, value)

        elif action == "remove":
            value = int(command[1])
            if value in arr:
                arr.remove(value)

        elif action == "append":
            value = int(command[1])
            arr.append(value)

        elif action == "sort":
            arr.sort()

        elif action == "reverse":
            arr.reverse()

        elif action == "pop":
            if arr:
                arr.pop()

        elif action == "print":
            print(arr)
