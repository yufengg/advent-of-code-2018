from collections import Counter 

def phase(filename):
  with open(filename, 'r') as f:
    read_data = f.read()
    num_str = read_data.split('\n')
    # print(len(num_str))

  sum = 0
  hist = Counter()
  while True:
    for n in num_str[:-1]:
      sum += int(n)

      hist[sum] += 1
      if hist[sum] == 2:
        print(sum)
        return sum

  print(sum)

if __name__ == "__main__":
  phase('input')
