reader_tests:
	python3 -m unittest tests/reader_tests.py

grid_tests:
	python3 -m unittest tests/grid_tests.py

rect_hole:
	python3 run_rect_hole.py

all:
	reader_tests
	grid_tests
