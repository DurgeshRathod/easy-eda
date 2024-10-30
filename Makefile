# Makefile for easy_eda project using Poetry

# Variables
PACKAGE_NAME = easy_eda
VERSION = 0.1.0
REPOSITORY = pypi  # Change this if you have a different repository

# Targets

.PHONY: all build clean install test publish

# Default target
all: build

# Build the package
build:
	poetry build

# Clean up previous builds
clean:
	rm -rf dist/ *.egg-info

# Install the package
install:
	poetry install

# Run tests
test:
	poetry run pytest

# Publish the package to PyPI or specified repository
publish:
	poetry publish --build
	


# Show help
help:
	@echo "Makefile for $(PACKAGE_NAME)"
	@echo ""
	@echo "Usage:"
	@echo "  make build      Build the package"
	@echo "  make clean      Clean up previous builds"
	@echo "  make install    Install the package and dependencies"
	@echo "  make test       Run tests using pytest"
	@echo "  make publish    Publish the package to PyPI"
	@echo "  make help       Show this help message"
