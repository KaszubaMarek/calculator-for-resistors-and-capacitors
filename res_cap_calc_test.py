from calculates import *


def test_res_weight_determination():
    # Try
    value_1 = 237
    value_2 = 2_370_000
    # When
    result_1 = res_weight_determination(value_1)
    result_2 = res_weight_determination(value_2)
    # Then
    assert result_1 == '237Ω '
    assert result_2 == '2.37MΩ '


def test_resistance_calculation_5_bands():
    # Try
    selected_colors = {'first_digit': 'Brown',
                       'second_digit': 'Red',
                       'third_digit': 'Black',
                       'multiplier': 'Orange',
                       'tolerance': 'Gold'
                       }
    # When
    result = resistance_calculation(selected_colors)
    # Then
    assert result == '120.0kΩ 5%'


def test_resistance_calculation_4_bands():
    # Try
    selected_colors = {'first_digit': 'Brown',
                       'second_digit': 'Red',
                       'third_digit': 'No band',
                       'multiplier': 'Orange',
                       'tolerance': 'Gold'
                       }
    # When
    result = resistance_calculation(selected_colors)
    # Then
    assert result == '12.0kΩ 5%'


def test_smd_3_numb_code_calc():
    # Try
    value = '213'
    # When
    result = smd_3_numb_code_calc(value)
    # Then
    assert result == '21.0kΩ 5%'


def test_smd_4_numb_code_calc():
    # Try
    value = '2104'
    # When
    result = smd_4_numb_code_calc(value)
    # Then
    assert result == '2.1MΩ 1%'


def test_smd_below_10_ohm_calc():
    # Try
    value1 = '2R5'
    value2 = '3R25'
    # When
    result1 = smd_below_10_ohm_calc(value1)
    result2 = smd_below_10_ohm_calc(value2)
    # Then
    assert result1 == '2.5Ω 5%'
    assert result2 == '3.25Ω 1%'


def test_smd_eia96_calc():
    # Try
    value1 = '78C'
    value2 = 'E11'
    value3 = 'B27'
    value4 = 'A59'
    # When
    result1 = smd_eia96_calc(value1)
    result2 = smd_eia96_calc(value2)
    result3 = smd_eia96_calc(value3)
    result4 = smd_eia96_calc(value4)
    # Then
    assert result1 == '63.4kΩ 1%'
    assert result2 == '2.7MΩ 2%'
    assert result3 == '1.2kΩ 5%'
    assert result4 == '680Ω 10%'


def test_capacitors_calc():
    # Try
    value = '336'
    # When
    result = capacitors_calc(value)
    # Then
    assert result == '33µF'


def test_cap_weight_determination():
    # Try
    value_in_pF = 470_000
    multiplier = 4
    # When
    result = cap_weight_determination(value=value_in_pF, multiplier=multiplier)
    # Then
    assert result == '470nF'


def test_capacitors_calc_below_10p():
    # Try
    value = '3R5'
    # When
    result = capacitors_calc_below_10p(value)
    # Then
    assert result == '3.5pF'
