""""Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example






: Append  to the list, .
: Append  to the list, .
: Insert  at index , .
: Print the array."""

if __name__ == '__main__':
    N = int(input())
    lista = []

    for _ in range(N):
        entrada = input().split()
        comando = entrada[0]
        if comando == "insert":
            lista.insert(int(entrada[1]), int(entrada[2]))
        elif comando == "print":
            print(lista)
        elif comando == "remove":
            lista.remove(int(entrada[1]))
        elif comando == "append":
            lista.append(int(entrada[1]))
        elif comando == "sort":
            lista.sort()
        elif comando == "pop":
            lista.pop()
        elif comando == "reverse":
            lista.reverse()
