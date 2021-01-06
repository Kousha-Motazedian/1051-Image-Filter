"""ECOR 1051 MILESTONE 2 Group:108
Submission Date: March 25th 2020
Designed By: Kousha Motazedian
             Mark Morgan
             Howard Wong
             Stephen Ogundayo"""

from Cimpl import set_color, create_color, copy, \
    get_height, get_width, load_image, choose_file, \
    get_color, Image, show


def grayscale(image: Image) -> Image:
    """
    Designed by: D.L. Bailey
    Return a grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        # Use the pixel's brightness as the value of RGB components for the
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.

        brightness = (r + g + b) // 3

        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int

        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
    return new_image


def combine(image_r: Image, image_g: Image, image_b: Image) -> Image:
    """Designed by: Kousha Motazedian
    Returns an image that has all of the r,g,b values of each pixel from image_R,
    image_G, and image_B.

    >>>combine(red_image, green_image, blue_image)
    new_image
    """
    new_image = copy(image_r)
    for x, y, (r, g, b) in new_image:
        r1, new_green, b = get_color(image_g, x, y)
        r2, g, new_blue = get_color(image_b, x, y)
        new_color = create_color(r, new_green, new_blue)
        set_color(new_image, x, y, new_color)

    return new_image


def _adjust_component(cc: int) -> int:
    """
    Designed By Kousha Motazedian
    Returns an int value assigned to cc depending on what value it was first
    assigned to.

    >>>_adjust_component(150)
    159
    """
    if cc <= 63:
        cc = 31
    if 64 <= cc <= 127:
        cc = 95
    if 128 <= cc <= 191:
        cc = 159
    if 192 <= cc <= 255:
        cc = 223

    return cc


def posterize(picture: Image) -> Image:
    """
    Designed By Kousha Motazedian
    Returns a new_image that is an altered form of picture where each RGB value
    of each pixel is put through the _adjust_component function.

    >>>posterize(image3)
    new_image
    """
    new_image = copy(picture)
    for x, y, (r, g, b) in new_image:
        new_r = _adjust_component(r)
        new_g = _adjust_component(g)
        new_b = _adjust_component(b)
        new_color = create_color(new_r, new_g, new_b)
        set_color(new_image, x, y, new_color)
    return new_image


def detect_edges_better(image: Image, threshold: float) -> Image:
    """
    Designed by Kousha Motazedian
    Returns a new image that looks as if it is a pencil sketch of image. The
    threshold value is the maximum tolerance of the difference of contrast before
    the pixel changes its color to black.

    >>>detect_edges_better(image_og,15)
    new_image
    """

    new_image = copy(image)
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    h = (get_height(new_image) - 1)
    w = (get_width(new_image) - 1)
    for x, y, (r, g, b) in new_image:
        if x == w or y == h:
            set_color(new_image, x, y, white)

        else:
            brightness1 = (r + g + b) / 3
            r1, g1, b1 = get_color(new_image, x + 1, y)
            brightness2 = (r1 + g1 + b1) // 3
            contrast1 = brightness1 - brightness2
            r2, g2, b2 = get_color(new_image, x, y + 1)
            brightness3 = (r2 + g2 + b2) // 3
            contrast2 = brightness1 - brightness3
            if abs(contrast1) > threshold or abs(contrast2) > threshold:
                set_color(new_image, x, y, black)
            else:
                set_color(new_image, x, y, white)

    return new_image


def green_channel(image: Image) -> Image:
    """
    Designed by: Mark Morgan
    Returns the copied image with the new rgb values to be (0,g,0) which results
    in a green filtered image. The function iterates through every pixel in the
    image and configures its rgb values. The new image is then stored and when
    called upon by the show() function the green filtered image is displayed.
    """
    new_image = copy(image)
    for pixel in new_image:
        x, y, (r, g, b) = pixel

        new_color = create_color(0, g, 0)
        set_color(new_image, x, y, new_color)

    return new_image


def two_tone(image: Image, colour1: str, colour2: str) -> Image:
    """
    Designed by: Mark Morgan
    Returns a copy of an image with colour1 and colour2 making up its tone.

    >>> two_tone(original_image, red, black)
    new_image
    """
    new_image = copy(image)
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    red = create_color(255, 0, 0)
    lime = create_color(0, 255, 0)
    blue = create_color(0, 0, 255)
    yellow = create_color(255, 255, 0)
    cyan = create_color(0, 255, 255)
    magenta = create_color(255, 0, 255)
    gray = create_color(128, 128, 128)

    colours = [("black", black), ("white", white), ("red", red), ("lime", lime), 
               ("blue", blue), ("yellow", yellow), ("cyan", cyan), 
               ("magenta", magenta), ("gray", gray)]

    for i in range(len(colours)):
        if colours[i][0] == colour1:
            colour1 = colours[i][1]
        if colours[i][0] == colour2:
            colour2 = colours[i][1]
    for x, y, (r, g, b) in new_image:
        brightness = (r + g + b) / 3
        if brightness >= 127:
            set_color(new_image, x, y, colour1)
        else:
            set_color(new_image, x, y, colour2)

    return new_image


def three_tone(image: Image, colour1: str, colour2: str, colour3: str) -> Image:
    """
    Designed by: Mark Morgan
    Returns a copy of an image in which colour1,colour2, and colour3 make up its 
    tone.
    >>>three_tone(image, "red", "black", "white")
    new_image
    """
    new_image = copy(image)

    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    red = create_color(255, 0, 0)
    lime = create_color(0, 255, 0)
    blue = create_color(0, 0, 255)
    yellow = create_color(255, 255, 0)
    cyan = create_color(0, 255, 255)
    magenta = create_color(255, 0, 255)
    gray = create_color(128, 128, 128)

    colours = [("black", black), ("white", white), ("red", red), ("lime", lime), 
               ("blue", blue), ("yellow", yellow), ("cyan", cyan), 
               ("magenta", magenta), ("gray", gray)]

    for i in range(len(colours)):
        if colours[i][0] == colour1:
            colour1 = colours[i][1]
        if colours[i][0] == colour2:
            colour2 = colours[i][1]
        if colours[i][0] == colour3:
            colour3 = colours[i][1]

    for x, y, (r, g, b) in new_image:
        brightness = (r + g + b) / 3

        if brightness <= 84:
            set_color(new_image, x, y, colour1)

        elif 85 <= brightness <= 170:
            set_color(new_image, x, y, colour2)

        else:
            set_color(new_image, x, y, colour3)

    return new_image


def detect_edge(image: Image, threshold: float) -> Image:
    """
    Designed by: Mark Morgan
    Returns the copy of an image that looks like a pencil sketch by detecting
    the edges of the image and changing them to black by comparing contrast to 
    threshold.

    >>>black = (0,0,0)
    >>>white = (255,255,255)

    brightness = average of r,g,b values
    contrast = abs(difference between brightness in top and bottom pixels)
    set to black if contrast > threshold

    >>>detect_edge(original_image,10)
    new_image
    """

    new_image = copy(image)
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    h = (get_height(new_image) - 1)
    w = (get_width(new_image) - 1)
    for x, y, (r, g, b) in new_image:
        if x == w or y == h:
            set_color(new_image, x, y, white)
        else:
            brightness1 = (r + g + b) / 3
            r1, g1, b1 = get_color(new_image, x, y + 1)
            brightness2 = (r1 + g1 + b1) // 3
            contrast1 = abs(brightness1 - brightness2)
            if contrast1 > threshold:
                set_color(new_image, x, y, black)
            else:
                set_color(new_image, x, y, white)

    return new_image


def blue_channel(image: Image) -> Image:
    """
    Designed by: Stephen Ogundayo
    Returns a blue copy of an image by turning the Red and Green components
    in each pixel to 0.

    >>>blue_channel(image)
    new_image
    """
    new_image = copy(image)

    for x, y, (r, g, b) in new_image:
        r_new = 0
        g_new = 0
        new_color = create_color(r_new, g_new, b)
        set_color(new_image, x, y, new_color)

    return new_image


def sepia(image: Image) -> Image:
    """
    Designed by: Stephen Ogundayo
    Returns an image that is a copy of image where the grayscale filter was 
    applied and is then tinted yellow.
    >>>sepia(image_1)
    gray
    """
    new_image = copy(image)
    gray = grayscale(new_image)

    for x, y, (r, g, b) in gray:
        if r < 63:
            b_new = b * 0.9
            r_new = r * 1.1
            new_color = create_color(r_new, g, b_new)
            set_color(gray, x, y, new_color)

        elif 63 <= r <= 191:
            b_new = b * 0.85
            r_new = r * 1.15
            new_color = create_color(r_new, g, b_new)
            set_color(gray, x, y, new_color)

        else:
            b_new = b * 0.93
            r_new = r * 1.08
            new_color = create_color(r_new, g, b_new)
            set_color(gray, x, y, new_color)

    return gray


def flip_horizontal(image: Image) -> Image:
    """ Designed by: Stephen Ogundayo
    Returns a new_image that is a copy of image that was flipped horizontally.
    >>>flip_horizontal(image_og)
    new_image
    """
    new_image = copy(image)
    w = get_width(new_image)
    h = get_height(new_image)
    h_middle = h // 2
    for y in range(h_middle):
        for x in range(w):
            rgb1 = get_color(new_image, x, y)
            rgb2 = get_color(new_image, x, h - 1 - y)
            set_color(new_image, x, y, rgb2)
            set_color(new_image, x, h - 1 - y, rgb1)

    return new_image


def red_channel(image: Image) -> Image:
    """
    Designed by: Howard Wong
    Returns a copy of the image with a red filter.

    >>>red_channel(image)
    new_image
    """
    new_image = copy(image)
    for x, y, (r, g, b) in new_image:
        g_new = 0
        b_new = 0
        new_color = create_color(r, g_new, b_new)
        set_color(new_image, x, y, new_color)

    return new_image


def extreme_contrast(image: Image) -> Image:
    """
    Designed by: Howard Wong
    Returns a copy of the image with extreme contrast filter applied to it.
    >>>extreme_contrast(image_og)
    new_image
    """

    new_image = copy(image)
    for x, y, (r, g, b) in new_image:
        if 0 <= r <= 127:
            r = 0
        else:
            r = 255
        if 0 <= g <= 127:
            g = 0
        else:
            g = 255
        if 0 <= b <= 127:
            b = 0
        else:
            b = 255
        new_color = create_color(r, g, b)
        set_color(new_image, x, y, new_color)

    return new_image


def flip_vertical(image: Image) -> Image:
    """
    Designed by: Howard Wong
    Returns a copy of image and vertically flips it.
    >>>flip_vertical(image_og)
    new_image
    """
    new_image = copy(image)
    w = get_width(new_image)
    h = get_height(new_image)
    w_middle = w // 2
    for x in range(w_middle):
        for y in range(h):
            rgb1 = get_color(new_image, x, y)
            rgb2 = get_color(new_image, w - 1 - x, y)
            set_color(new_image, x, y, rgb2)
            set_color(new_image, w - 1 - x, y, rgb1)

    return new_image
