import numpy


def main():

    racers = ("Piastri", "Russell", "Norris", "Leclerc", "Hamilton", "Verstappen", "Albon", "Tsunoda")

    print(racers)

    is_running = True

    while is_running:
        racer = input("Choose a racer: ")
        print()
        if racer.capitalize() == "Piastri":
            from piastri_stats import piastri_lap_lengths
            laps = piastri_lap_lengths
        elif racer.capitalize() == "Russell":
            from russell_stats import russell_lap_lengths
            laps = russell_lap_lengths
        elif racer.capitalize() == "Norris":
            from norris_stats import norris_lap_lengths
            laps = norris_lap_lengths
        elif racer.capitalize() == "Leclerc":
            from leclerc_stats import leclerc_lap_lengths
            laps = leclerc_lap_lengths
        elif racer.capitalize() == "Hamilton":
            from hamilton_stats import hamilton_lap_lengths
            laps = hamilton_lap_lengths
        elif racer.capitalize() == "Verstappen":
            from verstappen_stats import verstappen_lap_lengths
            laps = verstappen_lap_lengths
        elif racer.capitalize() == "Albon":
            from albon_stats import albon_lap_lengths
            laps = albon_lap_lengths
        elif racer.capitalize() == "Tsunoda":
            from tsunoda_stats import tsunoda_lap_lengths
            laps = tsunoda_lap_lengths

        print()
        laps.sort()
        num_of_laps = len(laps)
        total_len_laps = sum(laps)

        # MEAN
        mean = total_len_laps/num_of_laps

        print(f"The average of {racer.capitalize()}'s laps was approximately {mean:.2f} seconds.")

        # MEDIAN
        median = numpy.quantile(laps, 0.5)

        print(f"The median of {racer.capitalize()}'s laps was approximately {median:.2f} seconds.")

        # FIRST QUARTILE
        q1 = numpy.quantile(laps, 0.25)

        print(f"The 25th percentile of {racer.capitalize()}'s laps was approximately {q1:.2f} seconds.")

        # THIRD QUARTILE
        q3 = numpy.quantile(laps, 0.75)

        print(f"The 75th percentile of {racer.capitalize()}'s laps was approximately {q3:.2f} seconds.")

        # OUTLIERS
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = [laps for laps in laps if laps > upper_bound or laps < lower_bound]
        print(f"{racer.capitalize()}'s laps which are outliers were: {outliers}")
        print()
        another_racer = input("Choose another racer? (Y/N): ")

        if not another_racer.upper() == "Y":
            break


if __name__ == "__main__":
    main()
