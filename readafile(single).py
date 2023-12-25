import matplotlib.pyplot as plt
import pandas as pd
def quadratic_weather_model(time, a, b, c):
    temperature = a * (time ** 2) + b * time + c
    return temperature

def main():
    print("Quadratic Weather Modeling")
    print("==========================")

    try:
        file_path = 'wea2.csv'
        df = pd.read_csv(file_path)
        time_values = list(range(0, 11))
        plt.figure(figsize=(8, 6))

        for index, row in df.iterrows():
            x,y,z = row['a'], row['b'], row['c']
            temperature_values = [quadratic_weather_model(t, x, y, z) for t in time_values]
            plt.plot(time_values, temperature_values, marker='o', linestyle='-', label=f'a={x}, b={y}, c={z}')

        plt.title('Temperature Variation Over Time')
        plt.xlabel('Time')
        plt.ylabel('Temperature')
        plt.grid(True)
        plt.xlim(0, 10)
        plt.legend()
        plt.show()

    except FileNotFoundError:
        print("File not found. Please make sure 'wea2.csv' exists.")
main()
