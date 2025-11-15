build:
	@pandoc --pdf-engine=xelatex -t beamer -F mermaid-filter --slide-level=2 --toc-depth=1 --listing -o part1.pdf part1.md
	@pandoc --highlight-style=tango -V colorlinks=true -V linkcolor=blue -V urlcolor=blue -o ssh_setup.pdf ssh_setup.md
	@echo Build success.
