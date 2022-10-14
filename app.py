
import ec2_scripts.create_an_ec2_instance as create_ec2
import ec2_scripts.describe_all_ec2_instances as describe_ec2
import ec2_scripts.restart_all_ec2_instances as restart_ec2
import ec2_scripts.stop_all_ec2_instances as stop_ec2
import ec2_scripts.terminate_all_ec2_instances as terminate_ec2

import ec2_scripts.connect_with_ppk as connect_ppk
import constants

create_response = create_ec2.run(constants.APPLICATION_NAME, constants.AWS_LINUX_IMAGE_ID, constants.AWS_INSTANCE_TYPE, constants.KEY_NAME)
describe_response = describe_ec2.run()
restart_response = restart_ec2.run()
stop_response = stop_ec2.run()
terminate_response = terminate_ec2.run()

print(create_response)
print(describe_response)
print(stop_response)
print(terminate_response)

my_connection_instance = dict()
my_connection_instance['hostname'] = "test_name"
my_connection_instance['username'] = "test_name"
my_connection_instance['password'] = "test_pass"
my_connection_instance['ppk_file_path'] = "test_path"

connect_ppk.run(my_connection_instance, 'ls')



