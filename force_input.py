def multiple_of_6():
    """
    Returns a multiple o f6, keeps asking otherwise
    :return: int
    """
    try:
        n = input("Please give me a multiple of 6:")
        n = int(n)

        if n % 6 == 0:
           return n
        else:
            print("that is not s multiple of 6")
        # if n / 6 == n // 6
    except ValueError:
        print("that is not a valid number")


multiple_of_6()