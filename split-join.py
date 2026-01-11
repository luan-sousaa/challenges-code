

def split_and_join(line):
    #pegar a string completa e substuir os espacos por -
    #outra forma seria usando o metodo replace
    #line = line.replace(" ", "-")
    line = line.split(" ")
    line = "-".join(line)
    return line
    
if __name__ == '__main__':
    #input dos dados
    line = input()
    #chamada da funcao
    result = split_and_join(line)
    print(result)