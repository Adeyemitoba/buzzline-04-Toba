import json
import os
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from kafka import KafkaConsumer
from dotenv import load_dotenv
from utils.utils_logger import logger  # Ensure logging utility is available

# Load environment variables
load_dotenv()

# Kafka configuration
KAFKA_SERVER = os.getenv("KAFKA_SERVER", "localhost:9092")
KAFKA_TOPIC = os.getenv("PROJECT_TOPIC", "buzzline-topic")

# Data storage for visualization
window_size = 30
timestamps = collections.deque(maxlen=window_size)
categories = collections.defaultdict(lambda: collections.deque(maxlen=window_size))

# Set up Matplotlib figure
fig, ax = plt.subplots(figsize=(10, 6))

# Initialize the plot
ax.set_title("Category Frequency Over Time")
ax.set_xlabel("Timestamp")
ax.set_ylabel("Message Count")
bars = None

# Categories to track (ensure these match your producer data)
category_labels = ["humor", "tech", "food", "travel", "entertainment", "gaming", "other"]
for category in category_labels:
    categories[category] = collections.deque(maxlen=window_size)

# Function to consume messages and update data
def consume_messages():
    """
    Connects to Kafka topic and consumes messages.
    """
    try:
        logger.info(f"Connecting to Kafka topic: {KAFKA_TOPIC}")

        consumer = KafkaConsumer(
            KAFKA_TOPIC,
            bootstrap_servers=KAFKA_SERVER,
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
            auto_offset_reset='latest',  # Start from the latest messages
            enable_auto_commit=True
        )

        logger.info(f"Successfully connected to Kafka topic: {KAFKA_TOPIC}")

        for message in consumer:
            data = message.value
            timestamp = data.get("timestamp", time.strftime("%H:%M:%S"))
            category = data.get("category", "other")

            # Store in rolling window
            timestamps.append(timestamp)
            for cat in category_labels:
                if cat == category:
                    categories[cat].append(categories[cat][-1] + 1 if len(categories[cat]) > 0 else 1)
                else:
                    categories[cat].append(categories[cat][-1] if len(categories[cat]) > 0 else 0)

            logger.info(f"Received: {data}")

    except Exception as e:
        logger.error(f"Error consuming messages: {e}")

# Function to update the plot dynamically
def update_plot(frame):
    """
    Matplotlib animation function to update the stacked bar chart.
    """
    ax.clear()
    ax.set_title("Category Frequency Over Time")
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Message Count")
    ax.set_xticks(range(len(timestamps)))
    ax.set_xticklabels(timestamps, rotation=45, ha="right")

    # Prepare data for the stacked bar chart
    data = [list(categories[cat]) for cat in category_labels]
    bottom = [0] * len(timestamps)
    for i, cat_data in enumerate(data):
        ax.bar(range(len(timestamps)), cat_data, bottom=bottom, label=category_labels[i])
        bottom = [b + c for b, c in zip(bottom, cat_data)]

    ax.legend(loc="upper left")

# Start consuming messages in a separate thread
import threading
consumer_thread = threading.Thread(target=consume_messages, daemon=True)
consumer_thread.start()

# Start real-time visualization
ani = animation.FuncAnimation(fig, update_plot, interval=1000)
plt.tight_layout()
plt.show()
