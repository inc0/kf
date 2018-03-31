// plugin/plugin.go

package main

import (
	"fmt"
	"runtime"
)

func UpdateCmd() {
	fmt.Println("[plugin] NumGoroutine:", runtime.NumGoroutine())
}
