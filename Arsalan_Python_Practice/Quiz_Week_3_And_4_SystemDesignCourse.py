import numpy as np

# ---------------------------------------------------------
# Function 1: freq1
# Purpose:
#   Counts how many times each value appears in the vector
#   using numerical comparison (procedural approach).
# ---------------------------------------------------------
def freq1(vector, values):
    """
    vector : numpy array containing data
    values : iterable of possible values to count

    Returns:
        An array where each element represents
        how many times a value appears in 'vector'
    """
    return np.array([
        # Count how many elements in vector are equal to v
        len(vector) - np.count_nonzero(vector - v)
        for v in values
    ])


# ---------------------------------------------------------
# Function 2: freq2
# Purpose:
#   Counts frequencies using a dictionary (object-oriented style)
# ---------------------------------------------------------
def freq2(vector):
    """
    Takes a vector and returns the frequency of each unique value.
    Uses a dictionary to store counts.
    """
    frequency_dict = {}

    # Count occurrences of each value
    for value in vector:
        if value in frequency_dict:
            frequency_dict[value] += 1
        else:
            frequency_dict[value] = 1

    # Convert dictionary to ordered numpy array
    return np.array([
        frequency_dict[i]
        for i in range(min(frequency_dict.keys()), max(frequency_dict.keys()) + 1)
    ])


# ---------------------------------------------------------
# MAIN PROGRAM (Testing both methods)
# ---------------------------------------------------------
if __name__ == "__main__":

    # Generate a random array of integers between 0 and 9
    vector = np.array([np.random.randint(0, 10) for _ in range(100)])

    # Call both frequency functions
    print("Vector:", vector)
    print("freq1 output:", freq1(vector, range(10)))
    print("freq2 output:", freq2(vector))
