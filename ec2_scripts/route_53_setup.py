import boto3


def run():
    client = boto3.client('route53')
    return True

def list_hosted_zones():
    client = boto3.client('route53')
    response = client.list_hosted_zones()
    return response

def get_hosted_zone_id(url_to_find):
    client = boto3.client('route53')
    response = client.list_hosted_zones()
    for zone in response['HostedZones']:
        if(url_to_find == zone['Name']):
            return zone

def create_hosted_zone(name, vpc_id, region, callerReference):
    client = boto3.client('route53')
    response = client.create_hosted_zone(
        Name=f'{name}',
        VPC={
            "VPCRegion": f'{region}',
            "VPCId": f'{vpc_id}'
        },
        CallerReference=f'{callerReference}'
    )
    return response

def create_route_53_record(url, zone_id, set_identifier, ip_address, comment=None):
    client = boto3.client('route53')
    response = client.change_resource_record_sets(
        HostedZoneId=f'{zone_id}',
        ChangeBatch={
            "Comment": f'{comment}',
            "Changes": [
                {
                    "Action": "UPSERT",
                    "ResourceRecordSet": {
                        "Name": f'{url}',
                        "Type": "A",
                        "Weight": 1,
                        "TTL": 60,
                        "SetIdentifier": f'{set_identifier}',
                        "ResourceRecords": [
                            {
                                "Value": f'{ip_address}'
                            },
                        ]
                    }
                },
            ]
        }
    )

def update_route_53_record(url, set_identifier, ip_address ):
    host_zone_id = get_hosted_zone_id(url)
    host_zone_id = host_zone_id['Id'][1:len(host_zone_id['Id'])]
    return create_route_53_record(url, host_zone_id, set_identifier, ip_address)

def add_address_to_url(url, ip_address):
    return True


def remove_address_from_url(url, ip_address):
    return True


def list_ip_address(url):
    return True
