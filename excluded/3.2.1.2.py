#!/usr/bin/env python3
import sys
import pygal

from pygal.style import Style
custom_style = Style(colors=('#000000', '#000000', '#000000', '#000000'), stroke_width=5)
line_style={'width': 2}

xy_chart = pygal.XY(style=custom_style, order_min=0.1, show_legend= False, height=150, width=400, include_x_axis=True, include_y_axis=True)
#xy_chart.y_labels = -1, 0, 1, 2
#xy_chart.x_labels = -3, -2, -1, 0, 1, 2, 3
xy_chart.add('', [(x, (-x - 1)) for x in range(-3, -0, 1)], stroke_style=line_style)
xy_chart.add('', [(x, (x + 1)) for x in range(-1, 1, 1)], stroke_style=line_style)
xy_chart.add('', [(x, (1 - x)) for x in range(0, 2, 1)], stroke_style=line_style)
xy_chart.add('', [(x, (x - 1)) for x in range(1, 4, 1)], stroke_style=line_style)
xy_chart.render_to_png(sys.argv[1])
