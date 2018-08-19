.PHONY: clean docker

all: clean techio.yml

clean:
	@rm techio.yml

docker:
	docker build -t computingwithdata/bash projects/bash
	docker push computingwithdata/bash
	docker build -t computingwithdata/powershell projects/powershell
	docker push computingwithdata/powershell
	docker build -t computingwithdata/python projects/python
	docker push computingwithdata/python
	docker build -t computingwithdata/r-base projects/R
	docker push computingwithdata/r-base

techio.yml:
	@./generate-playground-config > techio.yml
	@./import-inline-code
