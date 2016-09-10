from livereload import Server, shell
server = Server()
# run a shell command
server.watch('./*', 'make static')


def alert():
    print('foo')
server.watch('foo.txt', alert)

# output stdout into a file
server.watch('./*', shell('lessc style.less', output='style.css'))

server.serve()
