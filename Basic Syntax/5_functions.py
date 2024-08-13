def function_one(test):
    print(test)


function_one("Hello!!!")  # Hello!!!


def function_two(*allArgs):
    print(allArgs)  # (1, 2, 3, 4)
    print(allArgs[0])  # 1
    print(allArgs[3])  # 4


function_two(1, 2, 3, 4)


def function_three(child3, child2, child1):
    print(child1)
    print(child3)


function_three(child1="Emil", child2="Tobias", child3="Linus")


def pass_function():
    pass


pass_function()


def receive_only_positional_arguments(arg1, /):
    print(arg1)


receive_only_positional_arguments(1)


def receive_only_keyword_arguments(*, arg1):
    print(arg1)


receive_only_keyword_arguments(arg1=2)


def return_none():
    pass


print(return_none)  # <function return_none at 0x000001FC4FB894E0>


def function_annotation(value: int = 2) -> bool:
    return True if value == 1 else False


print(function_annotation("1"))  # False
