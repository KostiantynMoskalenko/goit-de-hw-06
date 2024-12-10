from kafka import KafkaAdminClient
from configs import kafka_config
import shutil

# Create Kafka client
admin_client = KafkaAdminClient(
    bootstrap_servers=kafka_config['bootstrap_servers'],
    security_protocol=kafka_config['security_protocol'],
    sasl_mechanism=kafka_config['sasl_mechanism'],
    sasl_plain_username=kafka_config['username'],
    sasl_plain_password=kafka_config['password']
)


topics_list = admin_client.list_topics()
print(topics_list)

admin_client.delete_topics(topics=['KostyaM_building_sensors',
                                   'KostyaM_alert_Kafka_topic'
                                   ])

shutil.rmtree("/tmp/checkpoints-2", ignore_errors=False, onerror=None, dir_fd=None)
#shutil.rmtree("/tmp/checkpoints-3", ignore_errors=False, onerror=None, dir_fd=None)

topics_list = admin_client.list_topics()
print(topics_list)

# Close client
admin_client.close()