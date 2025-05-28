import numpy


def main():
    is_running = True

    racers = ("Piastri", "Russell", "Norris", "Leclerc", "Hamilton", "Verstappen", "Albon", "Tsunoda")
    print(racers)

    while is_running:
        racer = input("Choose a racer: ")
        print()
        if racer.capitalize() == "Piastri":
            from stats_piastri import piastri_lap_lengths
            laps = piastri_lap_lengths
        elif racer.capitalize() == "Russell":
            from stats_russell import russell_lap_lengths
            laps = russell_lap_lengths
        elif racer.capitalize() == "Norris":
            from stats_norris import norris_lap_lengths
            laps = norris_lap_lengths
        elif racer.capitalize() == "Leclerc":
            from stats_leclerc import leclerc_lap_lengths
            laps = leclerc_lap_lengths
        elif racer.capitalize() == "Hamilton":
            from stats_hamilton import hamilton_lap_lengths
            laps = hamilton_lap_lengths
        elif racer.capitalize() == "Verstappen":
            from stats_verstappen import verstappen_lap_lengths
            laps = verstappen_lap_lengths
        elif racer.capitalize() == "Albon":
            from stats_albon import albon_lap_lengths
            laps = albon_lap_lengths
        elif racer.capitalize() == "Tsunoda":
            from stats_tsunoda import tsunoda_lap_lengths
            laps = tsunoda_lap_lengths

        print()
        laps.sort()

        # RANGE

        shortest_lap = min(laps)
        longest_lap = max(laps)
        print(f"{racer.capitalize()}'s shortest recorded lap was {shortest_lap} seconds.")
        print(f"{racer.capitalize()}'s longest recorded lap was {longest_lap} seconds.")

        # MEAN
        num_of_laps = len(laps)
        total_len_laps = sum(laps)
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
            is_running = False


if __name__ == "__main__":
    main()

