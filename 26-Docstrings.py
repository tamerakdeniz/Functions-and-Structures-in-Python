def format_name(f_name, l_name):
    """TRYING
    WHAT'S COOKING
    HERE"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("Tamer", "Akdeniz")

length = len(formatted_name)

def my_function(num):
    """Multiplies a number by itself."""
    return num * num

print(my_function(10))