import pandas as pd

# MOM AGE AT BIRTH = R's mom age in 1979 - R's age in 1979
def mom_age_at_birth(df):
    def get_mom_age(row):
        # model a
        if row['R2303600'] > 0:
            result = row['R2303600'] - 8
            return result
        elif row['R2505800'] > 0:
            result = row['R2505800'] - 9
            return result

        # model b
        elif row['R2303500'] != 66 and row['R2303500'] > 0:
            result = 79 - row['R2303500']
            return result
        elif row['R2505700'] != 66 and row['R2505700'] > 0:
            result = 79 - row['R2505700']
            return result

        # model c
        else:
            conditions_c = [
                (row['R0175800'] == 5, row['R0175900'] > 0, row['R0175900']),
                (row['R0176700'] == 5, row['R0176800'] > 0, row['R0176800']),
                (row['R0177600'] == 5, row['R0177700'] > 0, row['R0177700']),
                (row['R0178500'] == 5, row['R0178600'] > 0, row['R0178600']),
                (row['R0179400'] == 5, row['R0179500'] > 0, row['R0179500']),
                (row['R0180300'] == 5, row['R0180400'] > 0, row['R0180400']),
                (row['R0181200'] == 5, row['R0181300'] > 0, row['R0181300']),
                (row['R0182100'] == 5, row['R0182200'] > 0, row['R0182200']),
                (row['R0183000'] == 5, row['R0183100'] > 0, row['R0183100']),
                (row['R0183900'] == 5, row['R0184000'] > 0, row['R0184000']),
                (row['R0184800'] == 5, row['R0184900'] > 0, row['R0184900'])
            ]

            for condition in conditions_c:
                if condition[0] and condition[1]:
                    result = condition[2]
                    return result

        return None

    df['mom_age'] = df.apply(get_mom_age, axis=1) - df['R0000600']

# DAD AGE AT BIRTH = R's dad age in 1979 - R's age in 1979
def dad_age_at_birth(df):
    def get_dad_age(row):
    # model a
        if row['R2303200'] > 0:
            result = row['R2303200'] - 8
            return result
        elif row['R2505400'] > 0:
            result = row['R2505400'] - 9
            return result

    # model b
        elif row['R2303100'] != 66 and row['R2303100'] > 0:
            result = 79 - row['R2303100']
            return result
        elif row['R2505300'] != 66 and row['R2505300'] > 0:
            result = 79 - row['R2505300']
            return result

    # model c
        else:
            conditions_c = [
            (row['R0175800'] == 4, row['R0175900'] > 0, row['R0175900']),
            (row['R0176700'] == 4, row['R0176800'] > 0, row['R0176800']),
            (row['R0177600'] == 4, row['R0177700'] > 0, row['R0177700']),
            (row['R0178500'] == 4, row['R0178600'] > 0, row['R0178600']),
            (row['R0179400'] == 4, row['R0179500'] > 0, row['R0179500']),
            (row['R0180300'] == 4, row['R0180400'] > 0, row['R0180400']),
            (row['R0181200'] == 4, row['R0181300'] > 0, row['R0181300']),
            (row['R0182100'] == 4, row['R0182200'] > 0, row['R0182200']),
            (row['R0183000'] == 4, row['R0183100'] > 0, row['R0183100']),
            (row['R0183900'] == 4, row['R0184000'] > 0, row['R0184000']),
            (row['R0184800'] == 4, row['R0184900'] > 0, row['R0184900'])
        ]

        for condition in conditions_c:
            if condition[0] and condition[1]:
                result = condition[2]
                return result

        return None


    df['dad_age'] = df.apply(get_dad_age, axis=1) - df['R0000600']

def age_at_birth_stats(df, parent):
    if parent == "mom":
        age_column = 'mom_age'
    elif parent == "dad":
        age_column = 'dad_age'
    else:
        raise ValueError("The input string must be either 'mom' or 'dad'.")

    filtered = df[df[age_column] >= 0]
    # Calculate the percentage of non-NaN values
    total_rows = len(df)
    filtered_rows = len(filtered)
    non_nan_count = filtered[age_column].count()
    percentage_non_nan = (non_nan_count / total_rows) * 100

    # Filter for teenage parents
    teenage_parents = filtered[filtered[age_column] < 21]
    percentage_teenage = (len(teenage_parents) / filtered_rows) * 100

    print(f"The percentage of non-NaN values in '{age_column}' is {percentage_non_nan:.2f}%")
    print(f"The percentage of teenage {parent} where '{age_column}' < 21 is {percentage_teenage:.2f}%")
