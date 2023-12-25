import matplotlib.pyplot as plt
def quadratic_temperature_model(day, a, b, c):
    temperature = a * day**2 + b * day + c
    return temperature

def main():
    # Hard-coded coefficients for the quadratic equation: ax^2 + bx + c
    a = float(input("Enter the quadratic coefficient (a): "))
    b = float(input("Enter the linear coefficient (b): "))
    c = float(input("Enter the constant term (c): "))

    # Get user input for the number of days to model
    num_days = int(input("Enter the number of days to model: "))

    days = list(range(1, num_days + 1))
    temperatures = [quadratic_temperature_model(day, a, b, c) for day in days]
    # Plotting
    plt.plot(days, temperatures, marker='o', label=f'Temperature: {a}x^2 + {b}x + {c}')
    plt.title('Weather Modeling')
    plt.xlabel('Day')
    plt.ylabel('Temperature (°C)')
    plt.grid()
    plt.legend()
    plt.show()
main()
