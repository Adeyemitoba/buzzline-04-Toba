# **buzzline-04-Toba**

This project visualizes real-time streaming data using a **stacked bar chart** to display the frequency of different categories over time. The data is streamed from a Kafka topic and dynamically processed by a Python consumer.

---

## **Overview**

This project demonstrates real-time data analysis and visualization using **Kafka** for streaming and **Matplotlib** for live plotting. It generates dynamic insights into category trends and provides meaningful visualizations as data flows into the system.

---

## **Features**

1. **Producer**:
   - Streams JSON messages to a Kafka topic (`project_json`).

2. **Consumer**:
   - Processes messages in real time.
   - Visualizes the data with:
     - **Stacked Bar Chart**: Displays the frequency of different categories (e.g., humor, tech, food) over time.

3. **Key Insights**:
   - Track trends in category frequency across a rolling window of the last 30 timestamps.
   - Identify dominant or trending categories in real-time.

---

## **Visualization**

### **Stacked Bar Chart: Category Frequency Over Time**
This chart dynamically updates to:
- Show message counts for each category (e.g., humor, tech, food).
- Visualize category trends over time using a rolling window.
- Provide insights into the most active categories at any given time.

---

## **Tools and Setup**

Before starting, ensure you have the following installed:

- **Python**: Version 3.11 or later.
- **Kafka**: With Zookeeper.
- **Python Libraries**:
  - `matplotlib`
  - `kafka-python`
  - `dotenv`

---

## **Prerequisites**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/buzzline-04-Toba.git
   cd buzzline-04-Toba

## **Install Dependencies:
pip install -r requirements.txt

## **Set Up Local Virtual Environment:
python -m venv .venv
.venv\Scripts\activate

## **Start Zookeeper and Kafka:

bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties

## **Start the Producer
.venv\Scripts\activate
python -m producers.project_producer_case

## **Start the Consumer
.venv\Scripts\activate
python -m consumers.project_consumer_Toba

## **Save Disk Space
To save disk space, you can delete the .venv folder when not actively working on the project. You can recreate and reactivate it later as needed.

## **License
This project is licensed under the MIT License. You are encouraged to fork, explore, and modify the code. See the LICENSE file for more details.
