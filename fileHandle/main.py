def calculate_sum(input_file, output_file):
    try:
        # Open the input file and read the numbers
        with open('./fileHandle/input.txt', 'r') as file:
            numbers = file.readlines()

        # Convert the read lines into integers and calculate the sum
        total_sum = sum(int(number.strip()) for number in numbers)

        # Write the sum to the output file
        with open( 'output.txt', 'w') as file:
            file.write(f"Sum of numbers: {total_sum}")

        print(f"Sum of numbers written to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = 'input.txt'  # Input file containing list of numbers
output_file = 'sum.txt'     # Output file to store the sum
calculate_sum(input_file, output_file)
