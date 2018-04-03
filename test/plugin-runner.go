// plugin-runner.go

package main

import (
	"os"
	"plugin"
	"time"
)

func main() {
	p, err := plugin.Open(os.Args[1])
	if err != nil {
		panic(err)
	}
	sym, err := p.Lookup("UpdateCmd")
	if err != nil {
		panic(err)
	}
	f := sym.(func())

	// Note that swapping these two lines makes the issue disappear
	// go f()
	f()

	time.Sleep(time.Second)
}
