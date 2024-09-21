import numpy as np

def create_frequency_distribution(data, num_classes):
    # Ensure data is a numpy array for convenience
    data = np.array(data)

    # Determine the range of the data
    min_value = np.min(data)
    max_value = np.max(data)
    range_value = max_value - min_value
    
    class_width = np.ceil(range_value / num_classes)
    if class_width % 2 == 1:
        class_width += 1
    # Create class limits
    class_limits = []
    for i in range(num_classes):
        lower_limit = min_value + i * class_width
        upper_limit = lower_limit + class_width
        class_limits.append((lower_limit, upper_limit))
    
    # Determine the frequencies
    frequencies = [0] * num_classes
    for value in data:
        for i, (lower_limit, upper_limit) in enumerate(class_limits):
            if lower_limit <= value < upper_limit:
                frequencies[i] += 1
                break
    
    return class_limits, frequencies

def main():
    # Read the number of classes
    num_classes = int(input("Enter the number of classes: "))

    # Read the raw data from the user
    raw_data = input("Enter the raw data separated by spaces: ").strip()
    data = list(map(float, raw_data.split()))
    
    # Create frequency distribution
    class_limits, frequencies = create_frequency_distribution(data, num_classes)
    
    # Print the frequency distribution
    print("\nFrequency Distribution:")
    for i, (limits, freq) in enumerate(zip(class_limits, frequencies)):
        print(f"Class {i+1}: {limits[0]:.2f} - {limits[1]:.2f} | Frequency: {freq}")

if __name__ == "__main__":
    main()