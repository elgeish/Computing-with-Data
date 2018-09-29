.PHONY: clean docker

all: clean techio.yml

clean:
	@rm techio.yml

docker:
	docker build -t computingwithdata/bash projects/sh
	docker push computingwithdata/bash
	docker build -t computingwithdata/cpp projects/cpp
	docker push computingwithdata/cpp
	docker build -t computingwithdata/java projects/java
	docker push computingwithdata/java
	docker build -t computingwithdata/powershell projects/ps1
	docker push computingwithdata/powershell
	docker build -t computingwithdata/python projects/py
	docker push computingwithdata/python
	docker build -t computingwithdata/r-base projects/R
	docker push computingwithdata/r-base

techio.yml:
	@./generate-playground-config > techio.yml
	@./import-inline-code
