# from collections import OrderedDict

BANDS_COLORS = {'Black': (0, '#000000'), 'Brown': (1, '#844200'), 'Red': (2, '#FF0000'),
                'Orange': (3, '#FF7F00'), 'Yellow': (4, '#FFFF00'), 'Green': (5, '#00FF00'),
                'Blue': (6, '#0000FF'), 'Violet': (7, '#AA55FF'), 'Grey': (8, '#808080'),
                'White': (9, '#FFFFFF'), 'Gold': (0.1, '#DCBA00'), 'Silver': (0.01, '#DBDBDB'),
                'No band': False}

TOLERANCE_COLORS = {'Brown': 1, 'Red': 2, 'Green': 0.5, 'Blue': 0.25, 'Violet': 0.1,
                    'Grey': 0.05, 'Gold': 5, 'Silver': 0.05, 'No color': 20}


def resistance_calculation(selected_bands: dict) -> str:
    if selected_bands['third_digit'] == 'No band':
        # resistor have 4 band code
        resistance: float = (BANDS_COLORS[selected_bands['first_digit']][0] * 10 +
                             BANDS_COLORS[selected_bands['second_digit']][0] * 1) \
                            * 10 ** BANDS_COLORS[selected_bands['multiplier']][0]
        tolerance_value: str = str(TOLERANCE_COLORS[selected_bands['tolerance']]) + '%'
        print('4 band code')
        result = weight_determination(resistance)

        return result + tolerance_value
    else:
        # resistor have 5 band code
        resistance: float = (BANDS_COLORS[selected_bands['first_digit']][0] * 100 +
                             BANDS_COLORS[selected_bands['second_digit']][0] * 10 +
                             BANDS_COLORS[selected_bands['third_digit']][0] * 1) \
                            * 10 ** BANDS_COLORS[selected_bands['multiplier']][0]
        tolerance_value: str = str(TOLERANCE_COLORS[selected_bands['tolerance']]) + '%'
        print('5 band code')
        result = weight_determination(resistance)
        return result + tolerance_value


def weight_determination(value: float) -> str:
    kilo: int = 10 ** 3
    mega: int = 10 ** 6
    giga: int = 10 ** 9
    tera: int = 10 ** 12

    if value >= tera:
        result = value/tera
        return str(result) + ' TΩ  '
    elif value >= giga:
        result = value/giga
        return str(result) + ' GΩ  '
    elif value >= mega:
        result = value/mega
        return str(result) + ' MΩ  '
    elif value >= kilo:
        result = value/kilo
        return str(result) + ' kΩ  '
    else:
        return str(value) + ' Ω  '


def smd_3_numb_code_calc(entry_value: str) -> str:
    value = int(entry_value[:2])
    multiplier = int(entry_value[2])
    resistance = value * 10 ** multiplier
    result = weight_determination(resistance)
    return result + '5%'


def smd_4_numb_code_calc(entry_value: str) -> str:
    value = int(entry_value[:3])
    multiplier = int(entry_value[3])
    resistance = value * 10 ** multiplier
    result = weight_determination(resistance)
    return result + '1%'


def smd_below_10_ohm_calc(entry_value: str) -> str:
    result = entry_value.upper().replace('R', '.')
    if len(result) >= 4:
        tolerance: str = '1%'
    else:
        tolerance = '5%'
    return str(result) + ' Ω  ' + tolerance


def smd_eia96_calc(entry_value: str) -> str:
    multipliers = {
        'Z': 0.001,
        'Y': 0.01,
        'R': 0.01,
        'X': 0.1,
        'S': 0.1,
        'A': 1,
        'B': 10,
        'H': 10,
        'C': 100,
        'D': 1000,
        'E': 10000,
        'F': 100000
                   }
    values_1_percent = {
        '01': 100, '02': 102, '03': 105, '04': 107, '05': 110, '06': 113, '07': 115,
        '08': 118, '09': 121, '10': 124, '11': 127, '12': 130, '13': 133, '14': 137,
        '15': 140, '16': 143, '17': 147, '18': 150, '19': 154, '20': 158, '21': 162,
        '22': 165, '23': 169, '24': 174, '25': 178, '26': 182, '27': 187, '28': 191,
        '29': 196, '30': 200, '31': 205, '32': 210, '33': 215, '34': 221, '35': 226,
        '36': 232, '37': 237, '38': 243, '39': 249, '40': 255, '41': 261, '42': 267,
        '43': 274, '44': 280, '45': 287, '46': 294, '47': 301, '48': 309, '49': 316,
        '50': 324, '51': 332, '52': 340, '53': 348, '54': 357, '55': 365, '56': 374,
        '57': 383, '58': 392, '59': 402, '60': 412, '61': 422, '62': 432, '63': 442,
        '64': 453, '65': 464, '66': 475, '67': 487, '68': 499, '69': 511, '70': 523,
        '71': 536, '72': 549, '73': 562, '74': 576, '75': 590, '76': 604, '77': 619,
        '78': 634, '79': 649, '80': 665, '81': 681, '82': 698, '83': 715, '84': 732,
        '85': 750, '86': 768, '87': 787, '88': 806, '89': 825, '90': 845, '91': 866,
        '92': 887, '93': 909, '94': 931, '95': 953, '96': 976
    }

    values_2_5_10_percent = {
        '01': 100, '02': 110, '03': 120, '04': 130, '05': 150, '06': 160, '07': 180,
        '08': 200, '09': 220, '10': 240, '11': 270, '12': 300, '13': 330, '14': 360,
        '15': 390, '16': 430, '17': 470, '18': 510, '19': 560, '20': 620, '21': 680,
        '22': 750, '23': 820, '24': 910, '25': 100, '26': 110, '27': 120, '28': 130,
        '29': 150, '30': 160, '31': 180, '32': 200, '33': 220, '34': 240, '35': 270,
        '36': 300, '37': 330, '38': 360, '39': 390, '40': 430, '41': 470, '42': 510,
        '43': 560, '44': 620, '45': 680, '46': 750, '47': 820, '48': 910, '49': 100,
        '50': 120, '51': 150, '52': 180, '53': 220, '54': 270, '55': 330, '56': 390,
        '57': 470, '58': 560, '59': 680, '60': 820
    }

    for key in multipliers.keys():
        entry_value = entry_value.upper()
        position = entry_value.find(key)
        if position == 0:
            value: int = values_2_5_10_percent[entry_value[1:]]
            multiplier: int = multipliers[entry_value[0]]
            resistance = value * multiplier
            result = weight_determination(resistance)
            if int(entry_value[1:]) < 25:
                tolerance: str = '2%'
            elif int(entry_value[1:]) < 49:
                tolerance = '5%'
            else:
                tolerance = '10%'

            return result + tolerance

        elif position == 2:
            value: int = values_1_percent[entry_value[:2]]
            multiplier: int = multipliers[entry_value[2]]
            resistance = value * multiplier
            result = weight_determination(resistance)
            tolerance: str = '1%'

            return result + tolerance


def capacitors_calc(entry_value: str) -> str:
    base: int = 10 ** -12
    piko: str = 'pF'
    nano: str = 'nF'
    mikro: str = 'uF'

    value: int = int(entry_value[:2])
    multiplier: int = int(entry_value[2])

    result = value * base * 10 ** multiplier

    return result


# 1R0 - 1R 5%
# 0R47 - 0,47R 1%
# 0R01 - 0,01R 1%
