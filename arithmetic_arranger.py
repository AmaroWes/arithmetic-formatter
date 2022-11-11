import re


def arithmetic_arranger(problems, out=False):
    output = out
    aux_lines, lines = [[],[],[],[]], [[],[],[],[]]

    if len(problems) > 5:
        return "Error: Too many problems."

    for i in problems:
        v = i.split(" ")
        result = 0

        if not re.findall("[+-]", v[1]):
            return "Error: Operator must be '+' or '-'."

        try:
            num_v_1 = int(v[0])
            num_v_2 = int(v[2])

            if len(v[0]) > 4 or len(v[2]) > 4:
                return "Error: Numbers cannot be more than four digits."

            if v[1] == '+':
                result = num_v_1 + num_v_2
            else:
                result = num_v_1 - num_v_2

        except ValueError:
            return "Error: Numbers must only contain digits."

        if len(v[0]) > len(v[2]):
            line_size = len(v[0]) + 2
        else:
            line_size = len(v[2]) + 2

        undeline = "-" * line_size
        aux_lines[0].append(" " * (line_size - len(v[0])) + v[0])
        aux_lines[1].append(v[1] + " " * (line_size - 1 - len(v[2])) + v[2])
        aux_lines[2].append(undeline)
        aux_lines[3].append(" " * (line_size - len(str(result))) + str(result))


    for i in range(len(aux_lines[0])):
        if lines[0]:
            aux = " " * 4
            lines[0][0] = lines[0][0] + aux + str(aux_lines[0][i])
            lines[1][0] = lines[1][0]  + aux + str(aux_lines[1][i])
            lines[2][0] = lines[2][0]  + aux + str(aux_lines[2][i])
            lines[3][0] = lines[3][0]  + aux + str(aux_lines[3][i])
        else:
            lines[0].append(str(aux_lines[0][i]))
            lines[1].append(str(aux_lines[1][i]))
            lines[2].append(str(aux_lines[2][i]))
            lines[3].append(str(aux_lines[3][i]))

    if output:
        arragend_problems = f"{lines[0][0]}\n{lines[1][0]}\n{lines[2][0]}\n{lines[3][0]}"
    else:
        arragend_problems = f"{lines[0][0]}\n{lines[1][0]}\n{lines[2][0]}"

    return arragend_problems
    