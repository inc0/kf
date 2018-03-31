
all:
	go build -o plugin/plugin.so -buildmode=plugin ./plugin
	go run plugin-runner.go plugin/plugin.so
