SUGAR=sugar
SOURCES=Sources/docommand.spy
PY_MODULE=Distribution/docommand.py
PREFIX=/usr/local

dist:
	$(SUGAR) -clpy $(SOURCES) | grep -v docommand.py > $(PY_MODULE) 
	chmod +x $(PY_MODULE)

doc:
	kiwi MANUAL.txt MANUAL.html

install:dist
	cp $(PY_MODULE) $(PREFIX)/bin/do

clean:
	rm _*.py *.pyc


