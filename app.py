
import ec2_scripts.create_an_ec2_instance as create_ec2
import ec2_scripts.describe_all_ec2_instances as describe_ec2
import ec2_scripts.restart_all_ec2_instances as restart_ec2
import ec2_scripts.stop_all_ec2_instances as stop_ec2
import ec2_scripts.terminate_all_ec2_instances as terminate_ec2

import ec2_scripts.connect_with_ppk as connect_ppk
import constants

#create_response = create_ec2.run(constants.APPLICATION_NAME, constants.AWS_LINUX_IMAGE_ID, constants.AWS_INSTANCE_TYPE, constants.KEY_NAME, [constants.AWS_DEPLOYMENT_SECURITY_GROUP])
#print(create_response)

describe_response = describe_ec2.run()
ec2_instance = describe_ec2.find_instance(constants.APPLICATION_NAME)

my_connection_instance = dict()
my_connection_instance['hostname'] = f'{ec2_instance["PublicDnsName"]}'
my_connection_instance['username'] = "ec2-user"
my_connection_instance['password'] = ""
my_connection_instance['ppk_file_path'] = "/ppk/Deployment-Key-Pair-OpenSSH"

print(connect_ppk.run(my_connection_instance, 'ls /'))



