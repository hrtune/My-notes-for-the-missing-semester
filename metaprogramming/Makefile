paper.pdf: paper.tex plot-data.png
	pdflatex paper.tex

# % : wildcard
# $* : pull from wildcard
# $@ : target file
plot-%.png: %.dat plot.py
	./plot.py -i $*.dat -o $@