""" "tkinker_color_chart.py" --- Creates a Color Chart for Python's Tkinker graphics module
    This program works with named colors. It includes a long list of names colors.
    The named colors are also useable in Python Turtle graphics.
Updated: June 5, 2023

Notes & Ref's:
0. This prg is available at https://github.com/python-can-define-radio/python-instructor/blob/main/misc/tkinker_color_chart.py
1a. This is a modified verision of: wpjohn, June 8, 2017, "Colors", wikiPython,
    https://www.wikipython.com/tkinter-ttk-tix/summary-information/colors/ , accessed Apr 4, 2023.
    Modifications include programming and order of the colors.
1b. Notes from wpjohn, who modified an earlier program, "If you want it smaller, 
    reduce the font size to 10 and delete the width=17 option. ...[The program]
    assign[s] fg [text color] to [be] black or white depending on luminance.
2. At least some Binomial colors can be written as a compound name double-capitalized.  
    E.g., 'deep pink' can also be written as 'DeepPink', similar to the numbered colors by that name.
3. Optionally, colors can be selected by specifying RGB (Red, green, Blue) values.  
    This method is not addressed here.
"""

import tkinter as tk

# Two lists of colors are given.  Located beyond the final list is a 
# 'COLORS' variable (all capital letters) to select which list will be displayed.

colors_sample = ['antique white', 'peach puff',
          'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
          'slate blue', 'medium blue', 'royal blue',  'blue',
          'dodger blue', 'deep sky blue', 'sky blue', 'steel blue', 'light steel blue',
          'dark turquoise', 'turquoise', 'cyan', 'cadet blue', 
          'medium aquamarine', 'aquamarine', 'dark green', 'dark sea green', 'sea green', 'medium sea green', 'spring green',
          'lawn green', 'lime green', 'forest green', 
          'yellow', 'gold', 'light goldenrod', 'goldenrod', 
          'SlateBlue4', 'RoyalBlue2', 'blue2', 'blue4',
          'DodgerBlue2', 'SteelBlue1', 'DeepSkyBlue2',  'SkyBlue2', 'LightSkyBlue2',
          'Slategray1', 'aquamarine2', 'DarkSeaGreen2', 'SeaGreen1', 
          'green2', 'green3', 'green4', 
          'orange', 'orange2', 'orange3', 'chocolate2', 'tomato', 'tomato3', 'orange red',  
          'brown1', 'red', 'red3', 'deep pink', 'hot pink',  'pink', 'pink2',
          'maroon', 'maroon3',  'VioletRed2', 'medium violet red', 'violet red',
          'magenta', 'magenta2', 'magenta3', 'orchid2', 'plum2',  'MediumOrchid2', 'DarkOrchid2',
          'purple2', 'MediumPurple2', 'blue violet', 'purple', 'medium purple', 
          'grey1', 'grey51', 'grey91', 'white']

colors = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
          'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
          'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
          'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
          'light slate gray', 'gray', 'light gray', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
          'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
          'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
          'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
          'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
          'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
          'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
          'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
          'indian red', 'saddle brown', 'sandy brown',
          'pale violet red', 'maroon', 'medium violet red', 'violet red',
          'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
          'thistle', 'snow2', 'snow3',
          'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
          'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
          'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
          'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
          'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
          'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
          'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
          'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
          'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
          'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
          'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
          'LightSkyBlue3', 'LightSkyBlue4', 'Slategray1', 'Slategray2', 'Slategray3',
          'Slategray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
          'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
          'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
          'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
          'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
          'cyan4', 'DarkSlategray1', 'DarkSlategray2', 'DarkSlategray3', 'DarkSlategray4',
          'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
          'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
          'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
          'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
          'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
          'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
          'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
          'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
          'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
          'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
          'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
          'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
          'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
          'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
          'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 
          'dark salmon', 'salmon', 'salmon1', 'salmon2',
          'salmon3', 'salmon4', 'light salmon', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 
          'orange', 'orange2', 'orange3', 'orange4', 'dark orange', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
          'coral', 'light coral', 'coral1', 'coral2', 'coral3', 'coral4', 
          'tomato', 'tomato2', 'tomato3', 'tomato4', 'orange red', 'OrangeRed2', 'OrangeRed3', 'OrangeRed4', 
          'red', 'red2', 'red3', 'red4', 'deep pink', 'DeepPink2', 'DeepPink3', 'DeepPink4',
          'hot pink', 'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink', 'pink1', 'pink2', 'pink3', 'pink4',
          'light pink', 'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
          'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
          'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
          'magenta', 'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
          'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
          'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
          'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
          'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
          'grey1', 'grey2', 'grey3', 'grey4', 'grey5', 'grey6', 'grey7', 'grey8', 'grey9', 'grey10',
          'grey11', 'grey12', 'grey13', 'grey14', 'grey15', 'grey16', 'grey17', 'grey18', 'grey19',
          'grey20', 'grey21', 'grey22', 'grey23', 'grey24', 'grey25', 'grey26', 'grey27', 'grey28',
          'grey29', 'grey30', 'grey31', 'grey32', 'grey33', 'grey34', 'grey35', 'grey36', 'grey37',
          'grey38', 'grey39', 'grey40', 'grey42', 'grey43', 'grey44', 'grey45', 'grey46', 'grey47',
          'grey48', 'grey49', 'grey50', 'grey51', 'grey52', 'grey53', 'grey54', 'grey55', 'grey56',
          'grey57', 'grey58', 'grey59', 'grey60', 'grey61', 'grey62', 'grey63', 'grey64', 'grey65',
          'grey66', 'grey67', 'grey68', 'grey69', 'grey70', 'grey71', 'grey72', 'grey73', 'grey74',
          'grey75', 'grey76', 'grey77', 'grey78', 'grey79', 'grey80', 'grey81', 'grey82', 'grey83',
          'grey84', 'grey85', 'grey86', 'grey87', 'grey88', 'grey89', 'grey90', 'grey91', 'grey92',
          'grey93', 'grey94', 'grey95', 'grey97', 'grey98', 'grey99', 'white']
 
""" Color List Selector """
# Choose one of the two color lists.  Make other a comment (#).
COLORS = colors  # Activate to display the large list
COLORS_NAME = "colors" # Activate to display the name of the list
# COLORS = colors_sample  # Activate to display an abrieviated list
# COLORS_NAME = "colors_sample" # Activate to display the name of the list


class ColorChart(tk.Frame):
 
    # MAX_ROWS = 41 # We found this needs to be in 'def __int__...', below
     
    FONT_SIZE = 12
     
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        if len(COLORS) > 100: 
            MAX_ROWS = 41  # Moved here to make it available.
        else: MAX_ROWS = 29
        BOX_WIDTH = int(17*(10/11))  # width of each color-sample box.
        r = 0
        c = 0
        myframe = tk.Frame(root)
        lumcheck = 32768
        for color in COLORS:
            label = tk.Label(self, text=color, bg=color, width=BOX_WIDTH,
                             font=("Times", self. FONT_SIZE, "bold"))
            colorlum = int(sum(root. winfo_rgb(color))/3)
            # if colorlum &amp;gt; lumcheck:
            if colorlum > lumcheck:
                label.configure(fg="grey4")
            else:
                label.configure(fg="snow")
 
            label.grid(row=r, column=c, sticky="ew")
            r += 1
            # if r &amp; gt; self.MAX_ROWS:
            if r == MAX_ROWS:
                r = 0
                c += 1
 
        self.pack(expand=1, fill="both")
 
 
if __name__ == '__main__':
    root = tk.Tk()
    sH = root.winfo_screenheight()
    sW = root.winfo_screenwidth()
    root.geometry(str(sW) + "x" + str(sH))
    root.title(f"Chart of Named Colors, using this list: '{COLORS_NAME}'")
    app = ColorChart(root)
    root.mainloop()
