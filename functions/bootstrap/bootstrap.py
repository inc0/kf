import os
import json
from subprocess import Popen, PIPE, STDOUT
import jinja2
import yaml
from kubernetes import client, config


def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)


def handler(event, context):
    data = json.loads(event['data'])
    context = {
        'pvc_path': 'null',
    }
    context.update(data)
    deploy_job = render("/bootstrap/deploy_job.yaml", context)
    p = Popen(['kubectl', 'create', '-f', '-'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    stdout = p.communicate(input=deploy_job.encode())[0]

    return stdout.decode()

