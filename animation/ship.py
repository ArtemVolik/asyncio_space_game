from itertools import cycle
import asyncio
from statistics import median
from tools import get_frame_size, draw_frame, read_controls


async def ship(canvas, frame1, frame2, max_row, max_col):

    frames = cycle([(frame1, frame2), (frame2, frame1)])
    ship_size_row, ship_size_col = get_frame_size(frame1)
    row = int(median(range(max_row - ship_size_row)))
    col = int(median(range(max_col - ship_size_col)))

    draw_frame(canvas, row, col, frame1)
    for frame in frames:

        draw_frame(canvas, row, col, frame[0], negative=True)
        row_offset, col_offset, _ = read_controls(canvas)

        if 0 <= row+row_offset <= max_row - ship_size_row:
            row = row + row_offset
        if 0 <= col+col_offset <= max_col - ship_size_col:
            col = col + col_offset

        draw_frame(canvas, row, col, frame[1])
        await asyncio.sleep(0)