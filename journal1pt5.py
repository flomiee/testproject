import math

def calculate_sin_table(start, end, entries):
    table_data = []
    step = (end - start) / (entries - 1)

    for i in range(entries):
        x = start + i * step
        y = math.sin(x)
        table_data.append((x, y))       
    return table_data

def print_table(data):
    print(f"{'x':<15} | {'sin(x)':<15}")
    print("-" * 33)
    for x, y in data:
        print(f"{x:<15.6f} | {y:<15.6f}")

def main():
    start_value = 0.0
    end_value = 2.0
    num_entries = 1000

    print(f"Generating a table for sin(x) between x = {start_value} and x = {end_value} with {num_entries} entries.")
    
    sin_table = calculate_sin_table(start_value, end_value, num_entries)
    print_table(sin_table)

if __name__=="__main__":
    main()