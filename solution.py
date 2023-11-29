import string

def solution(filename):
    """
    Expected return value is a dict
    """
    # Initialize variables
    shortest_words = []
    longest_words = []
    letter_count = {}
    word_count = 0
    line_count = 0

    # Open the file and process its content
    with open(filename, 'r') as file:
        for line in file:
            line_count += 1
            words = line.split()

            for word in words:
                # Check word length for shortest and longest words
                if not shortest_words or len(word) < len(shortest_words[0]):
                    shortest_words = [word]
                elif len(word) == len(shortest_words[0]):
                    shortest_words.append(word)

                if not longest_words or len(word) > len(longest_words[0]):
                    longest_words = [word]
                elif len(word) == len(longest_words[0]):
                    longest_words.append(word)

                # Count each letter/symbol occurrence
                for char in word:
                    if char in letter_count:
                        letter_count[char] += 1
                    else:
                        letter_count[char] = 1

                # Increment word count
                word_count += 1

    # Sort the letter count dictionary by keys
    sorted_letter_count = {k: v for k, v in sorted(letter_count.items())}

    # Print results to stdout
    print("Shortest word(s):", shortest_words)
    print("\nLetter/symbol count:")
    for char, count in sorted_letter_count.items():
        print(f"{char}: {count}")

    print("\nLongest word(s):", longest_words)
    print("\nWord count:", word_count)
    print("Line count:", line_count)

    # Return data in a dictionary
    return {
        "shortest_words": shortest_words,
        "letter_count": sorted_letter_count,
        "longest_words": longest_words,
        "word_count": word_count,
        "line_count": line_count
    }

# Example usage:
filename = "./minion-submissions/minion-1.txt"  # Replace with the actual file name
result = solution(filename)
print("\nReturned Data:")
print(result)
