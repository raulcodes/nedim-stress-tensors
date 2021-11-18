import numpy
"""
stress_tensor - (3x3) nparray
unit_vector   - (1x3) nparray

XX = (l_1 ** 2)t_xx + (m_1 ** 2)t_yy + (n_1 ** 2)t_zz + 2(m_1)(n_1)t_yz + 2(n_1)(l_1)t_zx + 2(l_1)(m_1)t_xy
"""
def normal_stress_component(st, uv):
    return numpy.around(sm(uv[0], st[0][0]) + sm(uv[1], st[1][1]) + sm(uv[2], st[2][2]) + (2*uv[1]*uv[2]*st[1][2]) + (2*uv[2]*uv[0]*st[0][2]) + (2*uv[0]*uv[1]*st[0][1]), decimals=2)

# square_multiply
def sm(l, t):
    return (l ** 2) * t

"""
stress_tensor - (3x3) nparray
unit_vector   - (1x3) nparray

XY = (l_1)(l_2)t_xx + (m_1)(m_2)t_yy + (n_1)(n_2)t_zz + ((m_1)(n_2) + (m_2)(n_1))t_yz + ((l_1)(n_2) + (l_2)(n_1))t_zx + ((l_1)(m_2) + (l_2)(m_1))t_xy
"""
def xy_stress_component(st, uv_1, uv_2):
    first_com = (uv_1[0]*uv_2[0]*st[0][0])+(uv_1[1]*uv_2[1]*st[1][1])+(uv_1[2]*uv_2[2]*st[2][2])
    second_com = ((uv_1[1]*uv_2[2] + uv_2[1]*uv_1[2])*st[1][2])+((uv_1[0]*uv_2[2]+uv_2[0]*uv_1[2])*st[0][2])+((uv_1[0]*uv_2[1]+uv_2[0]*uv_1[1])*st[0][1])
    return numpy.around(first_com + second_com, decimals=2)