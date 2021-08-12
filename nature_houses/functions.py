from pygame.draw import *

white = (255, 255, 255)
brown = (150, 75, 0)
red = (135, 80, 83)
lavender = (225, 229, 242)
green = (49, 73, 60)


def clouds(first_circle_center_x: int, first_circle_center_y: int, screen):
    """
    Making clouds
    :param first_circle_center_x: first (left) circle center x-coordinate
    :param first_circle_center_y: first (left) circle center y-coordinate
    :param screen: pygame screen
    :return: blank string
    """
    circle(screen, white, (first_circle_center_x, first_circle_center_y), 20, width=0)
    circle(screen, white, (first_circle_center_x + 20, first_circle_center_y), 20, width=0)
    circle(screen, white, (first_circle_center_x + 10, first_circle_center_y - 25), 20, width=0)
    circle(screen, white, (first_circle_center_x + 25, first_circle_center_y - 30), 20, width=0)
    circle(screen, white, (first_circle_center_x + 45, first_circle_center_y - 20), 20, width=0)
    circle(screen, white, (first_circle_center_x + 55, first_circle_center_y), 20, width=0)
    return ' '


# start point - top left house point
def house(top_left_house_x: int, top_left_house_y: int, screen):
    """
    Building a house
    :param top_left_house_x: top left x-coordinate of the house
    :param top_left_house_y: top left y-coordinate of the house
    :param screen: pygame screen
    :return: blank
    """
    rect(screen, brown, (top_left_house_x, top_left_house_y,
                         top_left_house_x - 20, top_left_house_y - 30), width=0)
    polygon(screen, red, [(top_left_house_x, top_left_house_y),
                          (top_left_house_x + 65, top_left_house_y - 100),
                          (top_left_house_x + 130, top_left_house_y)], width=0)
    rect(screen, lavender, (top_left_house_x + 50, top_left_house_y + 30,
                        top_left_house_x - 120, top_left_house_y - 110), width=0)
    return ' '


def tree(top_circle_x: int, top_circle_y: int, screen):
    """
    Making a tree
    :param top_circle_x: top circle x-coordinate
    :param top_circle_y: top circle y-coordinate
    :param screen: pygame screen
    :return: blank string
    """
    line(screen, brown, (top_circle_x, top_circle_y), (top_circle_x, top_circle_y + 60), width=15)
    circle(screen, green, (top_circle_x, top_circle_y - 40), 20, width=0)
    circle(screen, green, (top_circle_x - 20, top_circle_y - 20), 20, width=0)
    circle(screen, green, (top_circle_x + 15, top_circle_y - 10), 20, width=0)
    circle(screen, green, (top_circle_x - 5, top_circle_y), 20, width=0)
    circle(screen, green, (top_circle_x - 25, top_circle_y + 5), 20, width=0)
    circle(screen, green, (top_circle_x + 20, top_circle_y + 15), 20, width=0)
    return ''
