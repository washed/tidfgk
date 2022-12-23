FROM texlive/texlive:latest

WORKDIR /tmp/build/

ENTRYPOINT ["latexmk", "-pdf"]
