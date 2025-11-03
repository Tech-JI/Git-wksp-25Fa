build:
	@pandoc --pdf-engine=xelatex -t beamer -F mermaid-filter --slide-level=2 --toc-depth=1 --listing -o part1.pdf part1.md
	@echo Build success.
