FILENAME=2012-11-29-pyvo-cli
COMPILER=pdfcslatex
FLAGS=-shell-escape

${FILENAME}.pdf:
	${COMPILER} ${FLAGS} ${FILENAME}.tex
	${COMPILER} ${FLAGS} ${FILENAME}.tex
	${COMPILER} ${FLAGS} ${FILENAME}.tex

clean:
	rm -f *.log *.aux *.nav *.out *.snm *.toc *.vrb *.pyc
