# Task 1

def my_first_name(first_name):
    """
    A function that returns the first_name of anyone

    Args:
        string: input first name
    Returns:
        string: it returns the first_name inputted
    """
    return f"My first_name is {first_name} ,"


def my_last_name(last_name):
    """
    A function that returns the last_name of anyone

    Args:
        string: input last_name
    Returns:
        string: it returns the last_name inputted
    """
    return last_name


def full_name(first, last):
    """
    A function that concatenate the first name 
    and the last name that will be returned from those 2 functions above

    Args:
        first_name and last_name
    Returns:
        string: it returns the concatenated full_name
    """
    first = my_first_name(first)
    last = my_last_name(last)
    full_name = first + ' ' + last
    return f"My full name is {full_name}"


print(full_name('Ojo', 'Zainab'))


# Task 2
details = ['first_name', 'last_name', 'date of birth']


def my_list(list_arg):
    """
    A function that transform the name of the attributes to follow 
    the snake_case naming convention

    Args:
        list: A list containing elements
    Returns:
        All elements contained in the list including the transformed element
    """
    my_new_list = [element.replace(" ", "_") for element in list_arg]

    return my_new_list


print(my_list(details))


# Task 3
name = ['Mayowa', 'chizoba', 'Chigozie']


def name_check(name):
    """
    A  function that extract names that begin with a capital letter and 
    end with letter a. Also convert names that begin with a capital letter but
    doesn’t end with letter a and convert its last letter to letter a


    Args:
        list: A list containing elements
    Returns:
        it returna lsit of names that starts with capital letter and ends with a
    """

    my_names = []
    for element in name:
        if element.istitle() and element.endswith("a"):
            my_names.append(element)
        elif element.istitle() and not element.endswith("a"):
            new_name = element.replace(element[-1], 'a')
            my_names.append(new_name)

    return my_names


print(name_check(name))


# Task 4
marketing_customers = ["Wofai", "Zainab", "A4atullah"]


def marketing_customer_checks(market_customers):
    """
    A generic function that a function that fail 
    if what they have inside that list doesn’t look like a valid name, i.e contains 
    only alphapets.

    Args:
        list: A list containing elements
    Returns:
        the exact entry that is bad with a meaningful message
    """

    new_market_list = []
    for name in market_customers:
        if not name.isalpha():
            new_market_list.append(name)
        else:
            pass
    return f"Invalid input for customer {new_market_list}. Kindly correct the entry"


print(marketing_customer_checks(marketing_customers))
