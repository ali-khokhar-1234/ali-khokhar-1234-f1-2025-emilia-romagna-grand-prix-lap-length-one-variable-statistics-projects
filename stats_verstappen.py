def verstappen(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


verstappen(Name="Max Verstappen",
           Age=27,
           Nationality="Dutch",
           Team="Red Bull Racing",
           Position=1)

verstappen_lap_lengths = [81.131, 81.258, 81.218, 81.228, 80.977, 81.496, 81.206, 81.194, 81.257, 81.289, 81.510,
                          81.435, 81.402, 81.231, 81.276, 81.024, 80.856, 81.255, 81.206, 81.115, 81.161, 81.464,
                          81.254, 81.360, 81.079, 81.316, 81.579, 80.330, 80.347, 80.271, 80.120, 79.960, 79.706,
                          79.788, 79.755, 79.653, 79.639, 79.513, 79.553, 79.790, 80.167, 78.611, 78.214, 78.101,
                          78.220, 77.988, 78.037, 78.439, 78.399, 78.597, 78.589]
