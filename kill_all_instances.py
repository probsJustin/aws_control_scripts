import ec2_scripts.terminate_all_ec2_instances as terminate_ec2

terminate_response = terminate_ec2.run()
print(terminate_response)