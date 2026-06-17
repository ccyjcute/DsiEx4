import matplotlib.pyplot as plt

def merge_sort(values: list[int]) -> None:
    """
    values: The list of integers to sort.
    """
    if len(values) <= 1:
        return

    midpoint = len(values) // 2
    left_half = values[:midpoint]
    right_half = values[midpoint:]

    merge_sort(left_half)
    merge_sort(right_half)

    left_index = 0
    right_index = 0
    merged_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            values[merged_index] = left_half[left_index]
            left_index += 1
        else:
            values[merged_index] = right_half[right_index]
            right_index += 1

        merged_index += 1

    while left_index < len(left_half):
        values[merged_index] = left_half[left_index]
        left_index += 1
        merged_index += 1

    while right_index < len(right_half):
        values[merged_index] = right_half[right_index]
        right_index += 1
        merged_index += 1


def plot_values(values: list[int]) -> None:
    """Display the values as a line plot."""
    positions = range(len(values))
    plt.plot(positions, values)
    plt.show()


def main() -> None:
    """Plot a list before and after sorting it."""
    values = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    plot_values(values)
    merge_sort(values)
    plot_values(values)


if __name__ == "__main__":
    main()
