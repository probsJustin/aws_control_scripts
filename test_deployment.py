
import ec2_scripts.create_an_ec2_instance as create_ec2
import ec2_scripts.describe_all_ec2_instances as describe_ec2
import ec2_scripts.restart_all_ec2_instances as restart_ec2
import ec2_scripts.stop_all_ec2_instances as stop_ec2
import ec2_scripts.terminate_all_ec2_instances as terminate_ec2
import ec2_scripts.describe_ec2_instance_status as status_ec2
import ec2_scripts.waiter_ec2_instance as waiter_ec2
import ec2_scripts.route_53_setup as route_53
import ec2_scripts.connect_with_ppk as connect_ppk

import time
import constants

if(describe_ec2.get_instance_status_running(constants.APPLICATION_NAME)):
    print(f'Found running instance of application')
else:
    print(f'Creating instance of the application')
    create_response = create_ec2.run(constants.APPLICATION_NAME, constants.AWS_LINUX_IMAGE_ID, constants.AWS_INSTANCE_TYPE, constants.KEY_NAME, [constants.AWS_DEPLOYMENT_SECURITY_GROUP])
    print(f'Created Instances: {create_response}')

### find the instance
describe_response = describe_ec2.run()
ec2_instance = describe_ec2.find_instances_not_terminated(constants.APPLICATION_NAME)
print(f'Found instance:{ec2_instance}')

print(f'If this timesout, you can re-run it when it gets to the sleeping part.....')

### waits for it to be a thing
waiter_ec2.wait_for_status_ok(ec2_instance[0]['InstanceId'])

print(f'Waited for the ec2 instance to start.....')

### Setting up route53 record

print(f'Setting up route53 record entry for {constants.AWS_APPLICATION_URL}')

route_53.update_route_53_record(constants.AWS_APPLICATION_URL, 'set_identifier_example', ec2_instance[0]['PublicIpAddress'])

print(f'Creating Connection....')

my_connection_instance = dict()
my_connection_instance['hostname'] = f'{ec2_instance[0]["PublicDnsName"]}'
my_connection_instance['username'] = "ec2-user"
my_connection_instance['password'] = ""
my_connection_instance['ppk_file_path'] = "/ppk/Deployment-Key-Pair-OpenSSH"

print(f'Website to check: http://{ec2_instance[0]["PublicDnsName"]}')
print(f'Now running the commands to build the ec2 instance...')

print(connect_ppk.run(my_connection_instance, 'sudo yum -y install docker'))
print(connect_ppk.run(my_connection_instance, 'docker version'))

print(connect_ppk.run(my_connection_instance, 'sudo systemctl enable docker.service'))
print(connect_ppk.run(my_connection_instance, 'sudo systemctl start docker.service'))
print(connect_ppk.run(my_connection_instance, 'sudo systemctl status docker.service'))

print(connect_ppk.run(my_connection_instance, 'sudo docker run -d -p 5000:5000 digitalocean/flask-helloworld'))
print(connect_ppk.run(my_connection_instance, 'sudo yum -y install git'))
print(connect_ppk.run(my_connection_instance, 'git version'))
print(connect_ppk.run(my_connection_instance, 'sudo yum -y install httpd'))
print(connect_ppk.run(my_connection_instance, 'sudo systemctl start httpd'))
print(connect_ppk.run(my_connection_instance, 'ls -la '))
print(connect_ppk.run(my_connection_instance, 'git clone https://github.com/probsJustin/aws_control_scripts'))
print(connect_ppk.run(my_connection_instance, 'ls -la ./aws_control_scripts '))

print(f'Website to check: http://{ec2_instance[0]["PublicDnsName"]}')
print(f'If you do not want your ec2 instance to be deleted you should stop the process right now.... ')
print(f'..... sleeping ..... ')

time.sleep(80)
terminate_response = terminate_ec2.run()
print(terminate_response)





