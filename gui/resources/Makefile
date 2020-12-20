all:
ifeq ($(OS),Windows_NT)
	python cnv.py
else
	pyrcc5 -o __init__.py resources.qrc
endif

