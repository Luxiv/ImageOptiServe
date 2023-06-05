import pika
from utils.image_optimizer import optimize_image

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='image_queue')


def send_image_to_queue(image_path):
    """
    Sends an image path to the image queue for optimization.

    :param image_path: The path of the image to be optimized.
    :return: None
    """
    print("[X] image in queue.")
    optimize_image(image_path)



channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='image_queue', on_message_callback=send_image_to_queue)
