"""ECOR 1051 MILESTONE 3 P8 Group:108
Submission Date: April 1st 2020
Designed By: Kousha Motazedian
             Mark Morgan
             Howard Wong
             Stephen Ogundayo"""

from Cimpl import show, Image

from T108_image_filters import grayscale, combine, posterize, \
    detect_edges_better, green_channel, two_tone, three_tone, detect_edge, \
    blue_channel, sepia, flip_horizontal, red_channel, extreme_contrast, \
    flip_vertical


def apply_filter(image: Image, filter_name: str) -> Image:
    """
    Designed by: Kousha Motazedian
    Returns image that has been changed by a filter that was found from the 
    filter_name. The two tone filter will apply yellow and cyan to the image 
    and three tone applies yellow, cyan, and magenta.
    >>>apply_filter(image, "2")
    image (image with 2-tone filter)
    """
    if filter_name == "2":
        filter_name = two_tone
    elif filter_name == "X":
        filter_name = extreme_contrast
    elif filter_name == "T":
        filter_name = sepia
    elif filter_name == "P":
        filter_name = posterize
    elif filter_name == "3":
        filter_name = three_tone
    elif filter_name == "E":
        filter_name = detect_edge
    elif filter_name == "I":
        filter_name = detect_edges_better
    elif filter_name == "V":
        filter_name = flip_vertical
    elif filter_name == "H":
        filter_name = flip_horizontal
    else:
        print("Please choose a filter")
    if filter_name == two_tone:
        image = filter_name(image, "cyan", "yellow")
        show(image)
        return image
    elif filter_name == three_tone:
        image = filter_name(image, "yellow", "magenta", "cyan")
        show(image)
        return image
    elif filter_name == detect_edge:
        threshold = input("Threshold?: ")
        threshold = int(threshold)
        image = filter_name(image, threshold)
        show(image)
        return image
    elif filter_name == detect_edges_better:
        threshold = input("Threshold?: ")
        threshold = int(threshold)
        image = filter_name(image, threshold)
        show(image)
        return image
    else:
        image = filter_name(image)
        show(image)
        return image
