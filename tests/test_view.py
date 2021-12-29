import pytest
from .. import integral_view


def test1():
    input_data = [[78, 120, 126],
                  [122, 79, 214],
                  [146, 208, 119],
                  [74, 167, 129],
                  [28, 97, 3]]
    output_data = [[78, 120, 126],
                   [122, 243, 463],
                   [146, 475, 814],
                   [74, 570, 1038],
                   [28, 621, 1092]]
    assert integral_view.integral_view_final(input_data) == output_data


def test2():
    input_data = [[24, 53, 218],
                  [91, 127, 50],
                  [208, 212, 208],
                  [98, 190, 77],
                  [253, 209, 215]]
    output_data = [[24, 53, 218],
                   [91, 247, 462],
                   [208, 576, 999],
                   [98, 656, 1156],
                   [253, 1020, 1735]]
    assert integral_view.integral_view_final(input_data) == output_data


def test3():
    input_data = [[233, 254, 55],
                  [70, 13, 80],
                  [219, 70, 244],
                  [106, 108, 25],
                  [83, 145, 221]]
    output_data = [[233, 254, 55],
                   [70, 104, -15],
                   [219, 323, 448],
                   [106, 318, 468],
                   [83, 440, 811]]
    assert integral_view.integral_view_final(input_data) == output_data


def test4():
    input_data = [[252, 78, 58],
                  [213, 226, 119],
                  [239, 71, 68],
                  [112, 252, 46],
                  [104, 199, 213]]
    output_data = [[252, 78, 58],
                   [213, 265, 364],
                   [239, 362, 529],
                   [112, 487, 700],
                   [104, 678, 1104]]
    assert integral_view.integral_view_final(input_data) == output_data


def test5():
    input_data = [[45, 149, 32],
                  [223, 180, 202],
                  [239, 103, 75],
                  [83, 37, 245],
                  [84, 255, 54]]
    output_data = [[45, 149, 32],
                   [223, 507, 592],
                   [239, 626, 786],
                   [83, 507, 912],
                   [84, 763, 1222]]
    assert integral_view.integral_view_final(input_data) == output_data

