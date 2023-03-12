def arithmetic_arranger(problems, value=False):
  
  arranged_problems = ""
  
  first_num = []
  second_num = []
  operators=[]

  for problem in problems:
    operator = problem.split()[1]
    
    # Checking number of quations
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        print(arranged_problems)
    else:
        pass
        
    # Checking operators
    if operator == "+" or operator == "-":
        pass
    else:
        arranged_problems = "Error: Operator must be '+' or '-'."
        print(arranged_problems)

    # Checking length of numbers in equations

    numbers = []
    numbers.append(problem.split()[0])
    numbers.append(problem.split()[2])

    for num in numbers:
        if len(num) > 4:
            arranged_problems = "Error: Numbers cannot be more than four digits."
            print(arranged_problems)
        else:
            pass

    # Spliting the elemnts of the list "problems" to first number, operator and second number

    first_num.append(problem.split()[0])
    second_num.append(problem.split()[2])
    operators.append(problem.split()[1])


    # Creating lists for the rows of final print

  first_row = []
  second_row = []
  dashes = []
  results = []

    # Creating order of rows for the final print

  for x, y, z in zip(first_num, second_num, operators):
    spaces = "    "
    first_row.append( " " * ((max(len(x), len(y)))+2 - len(x)) + x + spaces)
    second_row.append( z + " " * ((max(len(x), len(y))) +1 - len(y)) + y + spaces)
    dashes.append("-" * ((max(len(x), len(y)))+2) + spaces)
    

    # Calculations for solution of equation

    result = []
    if z == "+":
        result= str(int(x) + int(y))
    else: 
        result= str(int(x) - int(y))

    results.append(" " * ((max(len(x), len(y)))- len(result) + 2) + result + spaces)

  row1 = " ".join(str(x) for x in first_row)
  row2 = " ".join(str(x) for x in second_row)
  row3 = " ".join(str(x) for x in dashes)

  row4 = " ".join(str(x) for x in results)


  if value == True:
        arranged_problems = print(row1 + "\n" +  row2 + "\n" +  row3 + "\n" +  row4)
  else:
        arranged_problems = print(row1 + "\n" +  row2 + "\n" +  row3 )


  return arranged_problems

