from collections import Counter 

def hash(str):
  word_code = 0
  for l in str:
    word_code += ord(l)
  return word_code

def read_file(filename):
  with open(filename, 'r') as f:
    read_data = f.read()
    split_str = read_data.split('\n')
  return split_str

def compare_codes(a,b):
  # print(f'comparing {a} and {b}')
  mismatch_ct = 0
  for i in range(len(a)):
    if a[i] != b[i]:
      # print(f'Letter difference in position {i}: {a[i]} vs {b[i]}')
      mismatch_ct += 1
    if mismatch_ct == 2:
      return False
  return True

def process(input_arr):
  count_list = 0
  count_compare = 0
  # map from hash code to a set of corresponding ID codes
  hash_set = dict()

  for code in input_arr:
    count_list +=1
    # print(code)
    # compute the hash, and insert the code at that location
    hashcode = hash(code)//26
    if hashcode in hash_set:
      # print(f'hash collision: {code}. Existing values: {hash_set[hashcode]}')
      hash_set[hashcode].add(code)
    else:
      hash_set[hashcode] = {code}
  print(f'number of codes: {count_list}')   

  # for (hash, set)
  for h,s in hash_set.items():
    for a in s:
      for b in s:
        count_compare +=1
        # This line is important -- without it it will compare the first code with itself and think that it's done
        if a != b:
          if compare_codes(a,b):
            print(f'number of comparisons: {count_compare}')
            return a,b

if __name__ == "__main__":
  input_arr = read_file('input')
  output = process(input_arr)
  print(output)
