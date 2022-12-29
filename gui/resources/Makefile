all:
ifeq ($(OS),Windows_NT)
	python cnv.py
else
	pyrcc5 resources.qrc -o resources.py
endif

