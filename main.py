import webcolors
import matplotlib.pyplot as plt

def closest_color(rgb):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - rgb[0]) ** 2
        gd = (g_c - rgb[1]) ** 2
        bd = (b_c - rgb[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

color = (223 , 241 , 224)

try:
    cname = webcolors.rgb_to_name(color)
    print(f"the color is exactly {cname}")
except ValueError:
    cname = closest_color(color)
    print(f"the color is closest to {cname}")

plt.imshow([[color]])
plt.show()