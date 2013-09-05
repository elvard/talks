FILENAME=2013-08-29-pyvo-testing-tools
COMPILER=pdfcslatex
FLAGS=-shell-escape

${FILENAME}.pdf:
	${COMPILER} ${FLAGS} ${FILENAME}.tex
	${COMPILER} ${FLAGS} ${FILENAME}.tex
	${COMPILER} ${FLAGS} ${FILENAME}.tex

clean:
	rm -f *.log *.aux *.nav *.out *.snm *.toc *.vrb *.pyc
