from collections import Counter 

def read_file(filename):
  with open(filename, 'r') as f:
    read_data = f.read()
    split_str = read_data.split('\n')
  return split_str

def process(input_arr):
  count_2 = 0
  count_3 = 0

  for code in input_arr:
    letters = Counter(code)
    has_2 = False
    has_3 = False
    for elem, ct in letters.items():
      if ct == 2:
        has_2 = True
      if ct == 3: 
        has_3 = True

    if has_2: count_2 += 1
    if has_3: count_3 += 1
  
  return count_2 * count_3
    

if __name__ == "__main__":
  input_arr = read_file('input')
  output = process(input_arr)
  print(output)
