.PHONY: all
all: barculator_*.c fooculator_*.c
	gcc barculator_abc.c -o barabc
	gcc barculator_abd.c -o barabd
	gcc barculator_acd.c -o baracd
	gcc barculator_bcd.c -o barbcd

	gcc fooculator_ab.c -o fooab
	gcc fooculator_ac.c -o fooac
	gcc fooculator_bc.c -o foobc

	gcc solver.c -o solver

run: all
	python3 runner.py

.PHONY: clean
clean:
	rm -rf out.txt
	rm -rf barabc barabd baracd barbcd fooab fooac foobc solver