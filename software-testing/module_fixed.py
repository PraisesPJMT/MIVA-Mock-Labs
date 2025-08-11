def crEate_mOdule(num_list):
    """Computes the sum and average of numbers in the list."""
    try:
        soma_total = sum(num_list)
        if len(num_list) == 0:
            raise ValueError("List is empty")
        media_val = soma_total / len(num_list)
        return soma_total, media_val
    except Exception as ex:
        print(f"Exception in crEate_mOdule: {ex}")
        return None, None

def str_concatenate(p1, p2):
    """Concatenates two strings with a space in-between."""
    try:
        concatenated = p1 + " " + p2
        return concatenated
    except Exception as ex:
        print(f"Exception in str_concatenate: {ex}")
        return ""

def division_operation(a, b):
    """Performs division of 'a' by 'b'."""
    try:
        quotient = a / b
        return quotient
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None

def list_indexing_example(items, idx):
    """Returns item at given index from list."""
    try:
        return items[idx]
    except IndexError:
        print(f"Index {idx} out of range for list!")
        return None

def main_executive():
    some_numbers = [10, 20, 30, 40, 50]
    totalout, averageout = crEate_mOdule(some_numbers)
    print("Total is:", totalout)
    print("Average is:", averageout)

    result = str_concatenate("MIVA", "Open University")
    print("Concatenated string:", result)

    div_result = division_operation(100, 0)
    print("Division Result:", div_result)

    sample_list = ["MIVA", "Open", "University"]
    print(list_indexing_example(sample_list, 5))


if __name__ == "__main__":
    main_executive()
