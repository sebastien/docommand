SUGAR=sugar
SOURCES=Sources/docommand.spy
PY_MODULE=Distribution/docommand.py

dist:
	$(SUGAR) -clpy $(SOURCES) > $(PY_MODULE)

doc:
	kiwi MANUAL.txt MANUAL.html
clean:
	rm _*.py *.pyc


