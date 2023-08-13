MYPY = mypy users posts utils
BLACK = black users posts utils
RUFF = ruff check posts users utils # --select I001 --fix
codefix:
	${BLACK}
	${RUFF}
	${MYPY}

# make codefix


