all:
	@echo "Makefile targets"
	@echo
	@echo "make all - this help"
	@echo "make serve - serve the prototype"

serve:
	@echo "Does not reload (yet) so restart after saving"
	python -m http.server
