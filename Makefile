SUGAR=sugar
SOURCES=Sources/docommand.spy
PY_MODULE=Distribution/docommand.py

dist:
	$(SUGAR) -clpy $(SOURCES) | grep -v docommand.py > $(PY_MODULE) 
	chmod +x $(PY_MODULE)

doc:
	kiwi MANUAL.txt MANUAL.html

clean:
	rm _*.py *.pyc


