NAME = 'getstats'
PACKAGE_NAME = 'getstats'

.PHONY: all
all: build

.PHONY: develop
develop: virtualenv
	. virtualenv/bin/activate && python3 setup.py develop || exit $$?; \

.PHONY: test
test: develop
	. virtualenv/bin/activate && python3 setup.py test

.PHONY: test-clean
test-clean:
	# Run after `make clean`
	test -z "$$($(GIT) clean --dry-run -dx)"

.PHONY: build
build: test virtualenv
	mkdir -p $@
	. virtualenv/bin/activate && python3 setup.py build

.PHONY: install
install: virtualenv
	python3 setup.py install

.PHONY: clean
clean: clean-build clean-test
	make METHOD=git sort-xml-files

.PHONY: clean-build
clean-build: clean-build-third-party clean-build-local

.PHONY: clean-build-third-party
clean-build-third-party:
	-$(RM) -r build

.PHONY: clean-build-local
clean-build-local:
	-$(RM) -r $(PACKAGE_NAME).egg-info
	-$(FIND) . -type d -name '__pycache__' -exec $(RM) -r {} +
	-$(FIND) . -type f -name '*.pyc' -delete

.PHONY: clean-test
clean-test:
	-$(RM) .coverage
	-$(RM) virtualenv

include configuration.mk
include make-includes/python.mk
include make-includes/variables.mk
include make-includes/xml.mk
