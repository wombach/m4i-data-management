'''
CONFLUENT KAFKA CREDENTIALS
'''
confluent_kafka = {
    "security.protocol": "SASL_SSL",
    "sasl.mechanisms": "PLAIN",
    "sasl.username": "YOUR_USERNAME",
    "sasl.password": "YOUR_PASSWORD"
}

'''
ELASTIC CREDENTIALS
'''
elastic = {
    "cloud_id": "YOUR_ELASTIC_CLOUD_ID",
    "http_auth": (
        "YOUR_USERNAME",
        "YOUR_PASSWORD"
    )
}

'''
FTE DATASET EBS CREDENTIALS
'''
fte_dataset = {
    "user": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD"
}
