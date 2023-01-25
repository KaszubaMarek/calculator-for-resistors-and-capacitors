from calculates import weight_determination, resistance_calculation

# @todo fix below function
def test_weight_determination():
    # Try
    value_1 = 237
    tolerance_1 = '5%'
    value_2 = 2_370_000
    tolerance_2 = '10%'
    # When
    result_1 = weight_determination((value_1, tolerance_1))
    result_2 = weight_determination((value_2, tolerance_2))
    # Then
    assert result_1 == '237 Ω  5%'
    assert result_2 == '2.37 MΩ  10%'

# @TODO: change variables implemented in function resistance calculation to dictionary
def test_resistance_calculation_5_bands():
    # Try
    selected_colors = {}
    first_band = 'Brown'
    second_band = 'Red'
    third_band = 'Black'
    multiplier = 'Orange'
    tolerance = 'Gold'
    # When
    result = resistance_calculation(first_band, second_band, third_band, multiplier, tolerance)
    # Then
    assert result == (120_000, '5%')


def test_resistance_calculation_4_bands():
    # Try
    first_band = 'Brown'
    second_band = 'Red'
    third_band = 'No band'
    multiplier = 'Orange'
    tolerance = 'Gold'
    # When
    result = resistance_calculation(first_band, second_band, third_band, multiplier, tolerance)
    # Then
    assert result == (12_000, '5%')


def test_smd_3_numb_code_calc():
    ...
    # Try
    # When
    # Then


def test_smd_4_numb_code_calc():
    ...
    # Try
    # When
    # Then


def test_smd_below_10_ohm_calc():
    ...
    # Try
    # When
    # Then


def test_smd_eia96_calc():
    ...
    # Try
    # When
    # Then


def test_capacitors_calc():
    ...
    # Try
    # When
    # Then