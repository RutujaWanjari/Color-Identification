# This is the main script to run.
# This program demonstrates how a color is identified from an image.

from PIL import Image
import closestcolorname


def avg_img_color(img):
    """
    Calculate average of individual red, green and blue colors.
    @param img: Actual RGB image
    @return int, int, int: Three average integer values of red, green and blue pixels respectively.
    """
    width, height = img.size
    r_total = 0
    g_total = 0
    b_total = 0
    count = 0

    # Compute total count of red, green and blue color pixel.
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x, y))
            r_total += r
            g_total += g
            b_total += b
            count += 1

    return r_total/count, g_total/count, b_total/count


def closest_color(avg_color):
    """
    To find actual color name. If actual color name is unknown then derive closest one. 
    @param avg_color: 
    @return actual_color_name:
    @return closest_color_name:
    """
    r = int(avg_color[0])
    g = int(avg_color[1])
    b = int(avg_color[2])
    requested_color = (r, g, b)
    print(requested_color)
    actual_color_name, closest_color_name = closestcolorname.get_colour_name(requested_color)

    return actual_color_name, closest_color_name


def commute_result(img):
    """
    Converting image of any form to RGB image and print result.
    @param img: 
    """
    img = img.convert('RGB')
    avg_color = avg_img_color(img)
    print("Actual and Closest color name are ", closest_color(avg_color))


# The redball.jpg image has a red colored ball with white background. Hence, closest color name is derived as
# lightcoral. light coral has approx 94% red, 50% green and 50% blue.
img = Image.open("redball.jpg")
commute_result(img)

# While the red.png is a fully red colored image. Hence, red color is derived.
img = Image.open("red.png")
commute_result(img)
