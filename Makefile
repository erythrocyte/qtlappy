reader_tests:
	python3 -m unittest tests/reader_tests.py

grid_tests:
	python3 -m unittest tests/grid_tests.py

geom_tests:
	python3 -m unittest tests/geom_tests.py

rect_hole:
	python3 run_rect_hole.py

all:
	reader_tests
	grid_tests
'examples/data/rect_hole/holes.txt'
    # fn_holes = os.path.join(dirname, fn_holes)
    # wells = holes_reader.read_holes_file(fn_holes)

    # gridMaker = gridTri2d.GridTri2D()
    # A = gridMaker.make_tri_grid(bound_points, wells)
    # B = tr.triangulate(A, 'qpa0.1')
    # ax = plt.axes()
    # # tr.compare(plt, A, B)
    # tr.plot(ax, **B)
    # ax.get_xaxis().set_visible(True)
    # ax.get_yaxis().set_visible(True)
    # plt.show()