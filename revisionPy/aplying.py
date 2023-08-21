# def print_square(size):
#   for i in range(size):
#     for j in range(size):
#       print("#",end="")
#     print("\n", end="")



# outra forma de printar o elemento em 2 dimensões

# dessa forma não precisamos criar 2 loops, apenas multiplicamos nosso # 
# em cada linha
def print_square(size):
    for i in range(size):
      print("#"* size)

print_square(3)