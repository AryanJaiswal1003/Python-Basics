""" ********* Hirst Painting Project [Part-1] ********* """

import colorgram

def diff_colors():
    # TODO-1: Extracting colors from the image & create an empty list
    colors = colorgram.extract('image.jpg' , 20)
    colouring = []
    # TODO-2: Iterate & loop over the extracted colors & store it in Tuple format, append it to the empty list
    """Loop over number_of_colors --> 20 & classifies it into r , g , b colors storing it & further looping."""
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        my_tuple = (r , g , b)
        colouring.append(my_tuple)
    print(colouring)


#TODO-3: Check colors values in https://www.w3schools.com/colors/colors_rgb.asp & remove values closer to white shade.

color_output_list = [(132, 166, 204), (220, 148, 108), (32, 41, 60), (197, 136, 149), (41, 106, 155), (141, 183, 162),
                     (164, 59, 49), (237, 212, 93), (147, 61, 68), (214, 83, 73), (52, 111, 91), (34, 61, 56),
                     (233, 167, 159), (157, 33, 30), (170, 29, 33), (15, 99, 71)]


"""Post extraction of colors the extraction function can be deleted since we don't need to extract colors again. """