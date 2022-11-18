init:
	pip install -r requirements.txt

clean:
	pip uninstall -r requirements.txt

test:
	tests
