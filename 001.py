raw_input = '''Insert Puzzle Input Here'''
#----------Functions--------------
def max_3_nums(contents, new_list):
  for x in range(3):
    max_num = max(contents)
    new_list.append(max_num)
    contents.remove(max_num)

  return new_list

#----------Formatting Input-------
puzzle_input = raw_input.splitlines()
blank_list, new_input, cal_list, final = [], [], [], []

for cal in puzzle_input:
  if cal == '':
    new_input.append(blank_list)
    blank_list = []
  else:
    blank_list.append(int(cal))
    
for list in new_input:
  cal_sum = sum(list)
  cal_list.append(cal_sum)
#----------Part One---------------
final = max_3_nums(cal_list, final)
print("The amount of calories that the elf with most calories is:", max(final))
#-----------Part Two--------------
print("The sum of the calories of the 3 elves with most calories is:", sum(final))
