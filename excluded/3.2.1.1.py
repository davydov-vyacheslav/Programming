#!/usr/bin/env python3
import sys
import pygal

from pygal.style import Style
custom_style = Style(colors=('#000000', '#000000', '#000000', '#000000'), stroke_width=5)
line_style={'width': 2}

xy_chart = pygal.XY(style=custom_style, order_min=0.1, height=150, width=400, include_x_axis=True, include_y_axis=True)
xy_chart.add('y = -1 / x', [(x / 10., (-10. / x)) for x in range(-50, -9, 1)], stroke_style=line_style)
xy_chart.add('y = x^2', [(x / 10., (x*x/100)) for x in range(-10, 11, 1)], stroke_style=line_style)
xy_chart.add('y = 1', [(x, 1) for x in range(1, 3, 1)], stroke_style=line_style)
xy_chart.render_to_png(sys.argv[1])