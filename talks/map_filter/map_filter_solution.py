import statistics
import string
import umpy_utils as utl

def is_temp_extreme(max_min_temps, max=70, min=50):
    """Return list of daily temperatures that falls between the specified
    < min > and < max > temperature range (inclusive).

    Parameters:
        max_min_temps (list): daily max and min temperatures
        max (int): upper bound max temperature
        min (int): lower bound min temperature

    Returns:
        bool: True if conditions met; otherwise False
    """

    return int(max_min_temps[0]) >= max and int(max_min_temps[1]) <= min


def to_celsius(temp):
    """Convert temperature measured on the Fahrenheit scale to Celsius.

    Parameters:
        temp (int): temperature value to convert

    Returns
        float: temperature value converted to Celsius
    """

    return round((int(temp) - 32) * .5556, 3)

def main():
    """Entry point."""

    # CHALLENGE 01: STR TO FLOAT

    filepath = './input/south_africa-life_expectancy-1960_2019.csv'
    data = utl.read_csv(filepath)

    headers = data[0]
    female_life_exp = data[1][4:]
    male_life_exp = data[2][4:]

    # Female life expectancy
    print(f"\nChallenge 01: female life expectancy (str) = {female_life_exp}")

    # map(): convert to int (working with a list)
    female_life_exp_flt = list(map(float, female_life_exp))

    print(f"\nChallenge 01: map(): female life expectancy (int) = {female_life_exp_flt}")

    # map(): convert to dict using dict()/zip(); convert values to float using map()
    female_life_exp_flt = dict(zip(headers[4:], map(float, female_life_exp)))

    print(f"\nChallenge 01: dict()/zip()/map(): female life expectancy = {female_life_exp_flt}")

    # Male life expectancy (dictionary comprehension)

    male_life_exp_flt = {headers[4:][i]: float(male_life_exp[i]) for i in range(len(headers[4:]))}

    print(f"\nChallenge 01: dict comp: male life expectancy (float) = {male_life_exp_flt}")


    # CHALLENGE 02: FAHRENHEIT TO CELSIUS

    filepath = './input/cape_town-temperature_readings-202106.csv'
    data = utl.read_csv(filepath)

    print(f"\nChallenge 02: Cape Town June max/min temps = {data[1:]}")

    # Separate the data
    headers = data[0]
    temp_max = [day[2] for day in data[1:]]
    temp_min = [day[3] for day in data[1:]]

    # Compute mean (average) max temperature (Fahrenheit)
    mean_max_temp_fahr = statistics.mean(map(int, temp_max))

    print(f"\nChallenge 02: map(): mean max temp (Fahrenheit) = {mean_max_temp_fahr}")

    # map(): compute mean (average) max temperature (Celsius)
    mean_max_temp_cels = statistics.mean(map(lambda x: round((int(x) - 32) * .5556, 3), temp_max))

    print(f"\nChallenge 02: map(): mean max temp (Celsius) = {mean_max_temp_cels}")

    # map(): convert max temp to Celsius
    temp_max_cels = list(map(lambda x: round((int(x) - 32) * .5556, 3), temp_max))

    print(f"\nChallenge 02: map(): temp max (Celsius) = {temp_max_cels}")

    # list comprehension: convert min temp to Celsius
    temp_min_cels = [round((int(temp) - 32) * .5556, 3) for temp in temp_min]

    print(f"\nChallenge 02: list comp: temp min (Celsius) = {temp_min_cels}")

    # Handle max/min temps (process two values)
    temp_max_min = [day[2:] for day in data[1:]] # returns nested lists

    temp_cels = [
        list(map(lambda x: round((int(x) - 32) * .5556, 3), max_min))
        for max_min in temp_max_min
    ]

    # Handle separate without map()
    # temp_cels = [
    #     [round((int(temp[0]) - 32) * .5556, 3), round((int(temp[1]) - 32) * .5556, 3)]
    #     for temp in temp_max_min
    # ]

    # temp_cels = []
    # for max_min in temp_max_min:
    #     temp_cels.append(list(map(lambda x: round((int(x) - 32) * .5556, 3), max_min)))

    print(f"\nChallenge 02: map(): temp max/min (Celsius) = {temp_cels}")

    # Rejoin with city and day values
    city_days = [day[:2] for day in data[1:]]
    cape_town_temps = [city_days[i] + temp_cels[i] for i in range(len(city_days))]

    print(f"\nChallenge 02: list comp: Cape Town June max/min temps (Celsius) = {cape_town_temps}")


    # CHALLENGE 03 FILTER()

    # Days temperature > 74 degrees Fahrenheit
    high_temps = list(filter(lambda x: int(x) >= 70, temp_max))

    # high_temps = filter(lambda x: int(x) >= 70, temp_max)
    # print(f"\nChallenge 03: Filter object = {type(high_temps)}")

    print(f"\nChallenge 03: filter(): Cape Town high temps (Fahrenheit) = {high_temps}")

    # Warn: can't pass arguments to function
    extreme_temps = list(filter(is_temp_extreme, temp_max_min))

    # Workaround: use lambda to pass args
    extreme_temps = list(filter(lambda x: is_temp_extreme(x, 68, 48), temp_max_min))

    print(f"\nChallenge 03: filter(): Cape Town extreme temps (Fahrenheit) = {extreme_temps}")


    # CHALLENGE 04: GET SPEECH
    # WARN: 1/2 lines in file are blank
    filepath = './input/mandela-prepared_speech.txt'

    # loop
    with open(filepath, 'r', newline='', encoding='utf-8') as file_obj:
        data_loop = []
        for line in file_obj:
            if line.strip(): # truth value (not None)
                data_loop.append(line)

    print(f"\nChallenge 04: loop: data length = {len(data_loop)}")
    print(f"\nChallenge 04: loop: last line = {data_loop[-1]}")

    # map()
    with open(filepath, 'r', newline='', encoding='utf-8') as file_obj:
        # This does not work; lambda needs an else:
        # data_map = list(map(lambda x: x.strip() if (x.strip()), file_obj.readlines()))

        # map() and filter()
        # data_map = list(map(lambda x: x.strip(), filter(lambda x: x.strip() != '', file_obj.readlines())))
        data_map = list(map(lambda x: x.strip(), filter(lambda x: x.strip(), file_obj.readlines())))

    print(f"\nChallenge 04: map()/filter(): data length = {len(data_map)}")
    print(f"\nChallenge 04: map()/filter(): last line = {data_map[-1]}")

    # list comprehension
    with open(filepath, 'r', newline='', encoding='utf-8') as file_obj:
        data_comp = [line.strip() for line in file_obj.readlines() if line.strip()]

    print(f"\nChallenge 04: comp: data length = {len(data_comp)}")
    print(f"\nChallenge 04: comp: last line = {data_comp[-1]}")


    # CHALLENGE 05: CLEAN DATA

    # 3-argument version of str.maketrans
    # arguments (x, y, z) where 'x' and 'y' must be equal-length strings
    # characters in 'x' are replaced by characters in 'y'
    # 'z' is string.punctuation where each character in the string is mapped to None

    translator = str.maketrans('', '', string.punctuation)

    # loop
    data_cleaned_loop = []
    for line in data_loop:
        data_cleaned_loop.append(line.translate(translator).lower())

    print(f"\nChallenge 05: loop: last line = {data_cleaned_loop[-1]}")

    # map()
    data_cleaned_map = list(map(lambda x: x.translate(translator).lower(), data_map))

    print(f"\nChallenge 05: map(): last line = {data_cleaned_map[-1]}")

    # list comprehension
    data_cleaned_comp = [line.translate(translator).lower() for line in data_comp]

    print(f"\nChallenge 05: comp: last line = {data_cleaned_comp[-1]}")


    # CHALLENGE 06: SEARCH (FILTER())

    search_term = 'apartheid'
    # search_term = 'white supremacy'
    # search_term = 'communist'
    # search_term = 'freedom charter'

    # filter()
    lines = list(filter(lambda x: search_term in x, data_cleaned_map))

    print(f"\nChallenge 06: filter: search len = {len(lines)}")
    print(f"\nChallenge 06: filter: search")
    for line in lines:
        print(f"\n{line}")

    # list comprehension
    lines = [line for line in data_cleaned_comp if search_term in line]

    print(f"\nChallenge 06: comp: search len = {len(lines)}")
    print(f"\nChallenge 06: comp: search")
    for line in lines:
        print(f"\n{line}")


if __name__ == '__main__':
    main()