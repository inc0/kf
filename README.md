# Client for kubeflow

## Requirements

[Kubeless](http://kubeless.io/) installed

## Usage

Deploy bootstrap function

`source kf/functions/deploy_me.sh`

Use CLI

`./kf env list`

Create kubeflow env

`./kf env create myenv`

Show kubeflow resources

`kubectl get po -n kubeflow-myenv`
