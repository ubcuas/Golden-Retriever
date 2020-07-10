## Util ##
list:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

## Run ##
run:
	python3 app.py

## Test ##
test:
	echo "Not done YET"

## Cleanup ##
clean:

## Install ##
install:

## Docker ##
docker:
	docker build . -t ubcuas/golden:latest

docker-publish: docker
	docker push ubcuas/golden:latest

## CI ##
ci-test:
	docker build . --target build -t ubcuas/golden:test
	# Insert test stuff HERE
