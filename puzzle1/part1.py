
def phase(filename):
  with open(filename, 'r') as f:
    read_data = f.read()
    num_str = read_data.split('\n')
    # print(len(num_str))

  sum = 0
  for n in num_str[:-1]:
    print(sum)
    sum += int(n)

  print(sum)

if __name__ == "__main__":
  phase('input')
