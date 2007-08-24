SUGAR=sugar
SOURCES=Sources/docommand.spy
PY_MODULE=Distribution/docommand.py

dist:
	$(SUGAR) -clpy $(SOURCES) > $(PY_MODULE)
clean:
	rm _*.py *.pyc


