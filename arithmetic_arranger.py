def arithmetic_arranger(problems, display = False):
  # All errors
  tooManyProblemsError = "Error: Too many problems."
  invalidOperatorError = "Error: Operator must be '+' or '-'."
  invalidInputError = "Error: Numbers must only contain digits."
  invalidLengthError = "Error: Numbers cannot be more than four digits."
  
  if len(problems) > 5:
    return tooManyProblemsError

  topLine, bottomLine, dashLine, answerLine = "", "", "", ""

  for i in problems:
    operand1, operator, operand2 = i.split()

    if operator not in ["+", "-"]:
      return invalidOperatorError

    if not operand1.isdigit() or not operand2.isdigit():
      return invalidInputError

    if len(operand1) > 4 or len(operand2) > 4:
      return invalidLengthError

    maxLength = max(len(operand1), len(operand2))

    topLine += operand1.rjust(maxLength + 2) + "    "
    bottomLine += operator + operand2.rjust(maxLength + 1) + "    "
    dashLine += "-" * (maxLength + 2) + "    "

    if display is True:
      if operator == "+":
        answer = str(int(operand1) + int(operand2))
      else:
        answer = str(int(operand1) - int(operand2))

      answerLine += answer.rjust(maxLength + 2) + "    "

  arranged_problem = topLine.rstrip() + "\n" + bottomLine.rstrip() + "\n" + dashLine.rstrip()
  
  if display is True:
    arranged_problem += "\n" + answerLine.rstrip()

  return arranged_problem
