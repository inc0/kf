#!/bin/bash

cobra init github.com/kkasravi/kf
cd $GOPATH/src/github.com/kkasravi/kf
cobra add create
cobra add delete
cobra add exec
cobra add logs
cobra add remove
cobra add shell
cobra add use
cobra add whoami
cobra add user
cobra add add -p 'userCmd'
cobra add rm -p 'userCmd'
cobra add list -p 'userCmd'
