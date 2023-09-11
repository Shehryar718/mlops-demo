# Makefile for Python project

install:
	@echo "Installing project dependencies..."
	pip install -r requirements.txt
	@echo "Installation complete."

test:
	@echo "Running tests..."
	pytest test.py
	@echo "Tests complete."
