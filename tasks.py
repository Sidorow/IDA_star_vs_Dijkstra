from invoke import task

@task
def start(ctx):
	ctx.run("python3 Project/src/index.py", pty=True)

@task
def test(ctx):
	ctx.run("coverage run --branch -m pytest", pty=True)

@task
def lint(ctx):
        ctx.run("pylint Project/src", pty=True)
