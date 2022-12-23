.PHONY: watch pdf clean-temp clean enable-roboto

build:
	docker-compose up --build --remove-orphans

watch:
	latexmk -pvc

pdf:
	latexmk -pdf

clean-temp:
	latexmk -c

clean:
	latexmk -C

enable-roboto:
	sudo updmap --sys --enable Map roboto.map
