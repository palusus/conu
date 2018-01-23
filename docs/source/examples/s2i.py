from conu import S2IDockerImage, DockerBackend

# to make sure that temporary directory is cleaned
with DockerBackend():
    source = 'https://github.com/dbarnett/python-helloworld'
    image = S2IDockerImage("centos/python-35-centos7")
    image.pull()
    extended_image = image.extend(source, "myapp")
    container = image.run_via_binary()

    container.stop()
    container.delete()
