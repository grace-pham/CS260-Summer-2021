import random
from bst import *


def _generate_value_list(list_size):
    value_list = []
    for i in range(list_size):
        value = random.randint(0, list_size * 5)
        value_list.append(value)
    return value_list


def _compute_bst_height(value_list):
    bst = BST()
    for value in value_list:
        bst.insert(value)
    height = bst.height()
    return height


def get_avg_height(number_of_elements):
    height_list = []
    for i in range(0, 5):
        value_list = _generate_value_list(number_of_elements)
        height = _compute_bst_height(value_list)
        height_list.append(height)
    avg = sum(height_list) / 5
    print(
        "| {:^19} | {:^15} | {:^15} | {:^15} | {:^15} | {:^15} | {:^15} |".format(number_of_elements, height_list[0],
                                                                                  height_list[1], height_list[2],
                                                                                  height_list[3], height_list[4], avg))


if __name__ == "__main__":
    print(
        "| Number Elements (n) | Height (Exp. 1) | Height (Exp. 2) | Height (Exp. 3) | Height (Exp. 4) | Height "
        "(Exp. 5) | Height (Average)|")

    number_of_element_list = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    for number_of_element in number_of_element_list:
        get_avg_height(number_of_element)
