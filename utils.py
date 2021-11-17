from IPython.display import display, Markdown, Math, Latex

import math
import numpy as np
import re

def parse_input(t):
    T_array = np.zeros(3)

    tensor_matrix_regexp = r"(\-*\s*\w*)([ijk])"
    matches = re.findall(tensor_matrix_regexp, t)
    if matches:
        if len(matches) > 3 or len(matches) == 0:
            raise Exception('Please enter a valid stress tensor')
        for item in matches:
            sanitized_value = item[0].replace(" ", "")
            if sanitized_value == '':
                sanitized_value = "1"
            if item[1] == 'i':
                T_array[0] = sanitized_value
            elif item[1] == 'j':
                T_array[1] = sanitized_value
            elif item[1] == 'k':
                T_array[2] = sanitized_value
    return T_array

def parse_unit_vector_input(t):
    T_array = np.zeros(3)

    tensor_matrix_regexp = r"(\-*\s*\S*)([ijk])"
    matches = re.findall(tensor_matrix_regexp, t)
    if matches:
        if len(matches) > 3 or len(matches) == 0:
            raise Exception('Please enter a valid stress tensor')
        for item in matches:
            print(item)
            sanitized_value = item[0].replace(" ", "")
            if sanitized_value == '':
                sanitized_value = "1"
            sanitized_value = sanitized_value.replace("sqrt", "math.sqrt")
            sanitized_value = eval(sanitized_value)
            if item[1] == 'i':
                T_array[0] = sanitized_value
            elif item[1] == 'j':
                T_array[1] = sanitized_value
            elif item[1] == 'k':
                T_array[2] = sanitized_value
    return T_array

def display_input(ist, T_x, T_y, T_z, N_1, N_2, N_3):
    display(Markdown("## Input"))
    display(Math(r"Tx: {} \\Ty: {} \\Tz: {}".format(T_x, T_y, T_z)))
    display(Latex(r"""\begin{{bmatrix}}
        {}_i & {}_j & {}_k \\
        {}_i & {}_j & {}_k \\
        {}_i & {}_j & {}_k
    \end{{bmatrix}}""".format(ist[0][0], ist[0][1], ist[0][2], ist[1][0], ist[1][1], ist[1][2], ist[2][0], ist[2][1], ist[2][2])))
    display(Math(r"N1: {} \\N2: {} \\N3: {} \\".format(N_1, N_2, N_3)))