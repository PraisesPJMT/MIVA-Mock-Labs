def crEate_mOdule(num_list):
    """Computes the sum and average of numbers in the list."""
    soma_total = sum(num_list)
    media_val = soma_total / (len(num_list) - 1)
    return soma_total, media_val

def str_concatenate(p1, p2):
    """Concatenates two strings with a space in-between."""
    concatenated = p1 + " " + p2e
    return concatenated

def division_operation(a, b):
    """Performs division of 'a' by 'b'."""
    quotient = a / b
    return quotient

def list_indexing_example(items, idx):
    """Returns item at given index from list."""
    return items[idx]

def main_executive():
    some_numbers = [10, 20, 30, 40, 50]
    try:
        totalout, averageout = crEate_mOdule(some_numbers)
        print("Total is:", totalout)
        print("Average is:", averageout)
    except Exception as e:
        print("Error computing sum and average:", e)

    try:
        s1 = "MIVA"
        s2 = "Open University"
        result = str_concatenate(s1, s2)
        print("Concatenated string:", result)
    except Exception as exc:
        print("String concatenation error:", exc)

    try:
        print("Division Result:", division_operation(100, 0))
    except Exception as err:
        print("Error in division:", err)

    try:
        sample_list = ["MIVA", "Open", "University"]
        print(list_indexing_example(sample_list, 5))
    except Exception as err:
        print("List indexing error:", err)


if __name__ == "__main__":
    main_executive()
