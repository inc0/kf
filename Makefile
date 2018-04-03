
all:
	#go build -o plugin/plugin.so -buildmode=plugin ./plugin
	go run main.go command add foobar
