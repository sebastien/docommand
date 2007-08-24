SUGAR=sugar
SOURCES=Sources/docommand.spy
PY_MODULE=Distribution/docommand.py

clean:
	rm _*.py *.pyc

build:
	$(SUGAR) -clpy $(SOURCES) > $(PY_MODULE)
