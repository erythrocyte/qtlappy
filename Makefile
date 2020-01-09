reader_tests:
	python3 -m unittest tests/reader_tests.py

grid_tests:
	python3 -m unittest tests/grid_tests.py

all:
	reader_tests
	grid_tests
