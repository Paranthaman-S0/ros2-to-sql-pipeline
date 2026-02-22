# ROS2 to SQL Pipeline - Turtlesim Data Engineering

A data engineering pipeline that captures ROS2 turtlesim pose data, logs it to CSV, and stores it in a SQLite database for analysis.

## Overview

This project demonstrates a complete data pipeline:
1. **Data Collection**: ROS2 node subscribes to turtlesim pose messages
2. **Data Logging**: Pose data (position, velocity, orientation) is logged to CSV
3. **Data Transformation**: ETL pipeline processes CSV data and loads it into SQLite database

## Project Structure

```
de_ros2/
├── turtle_pose_logger.py    # ROS2 node for capturing turtle pose data
├── etl.py                   # ETL pipeline for data transformation and loading
├── turtle_pose.csv          # CSV log of turtle pose data (generated)
├── turtle_data.db           # SQLite database with processed data (generated)
└── README.md               # This file
```

## Prerequisites

- ROS2 (Humble or later)
- Python 3.8+
- turtlesim package
- rclpy

## Installation

1. Install dependencies:
```bash
sudo apt-get install ros-humble-turtlesim
pip install rclpy
```

2. Source ROS2 setup:
```bash
source /opt/ros/humble/setup.bash
```

## Usage

### 1. Start the Turtlesim Node

```bash
ros2 run turtlesim turtlesim_node
```

### 2. Run the Turtle Pose Logger

In another terminal:
```bash
python3 turtle_pose_logger.py
```

This will:
- Subscribe to `/turtle1/pose` topic
- Log all pose data to `turtle_pose.csv`
- Continue logging until you press Ctrl+C

### 3. Run the ETL Pipeline

```bash
python3 etl.py
```

This will:
- Read data from `turtle_pose.csv`
- Transform and clean the data
- Load it into `turtle_data.db` SQLite database

## Data Schema

### CSV Format (turtle_pose.csv)
```
time,x,y,theta,linear_velocity,angular_velocity
2026-02-22T14:30:45.123456,5.544444,5.544444,0.0,0.0,0.0
...
```

### SQLite Table Structure
Data is stored in a `turtle_pose` table with columns:
- `id` (INTEGER PRIMARY KEY)
- `timestamp` (TEXT)
- `x` (REAL)
- `y` (REAL)
- `theta` (REAL)
- `linear_velocity` (REAL)
- `angular_velocity` (REAL)

## Files

### turtle_pose_logger.py
ROS2 node that:
- Creates a TurtlePoseLogger node
- Subscribes to `/turtle1/pose` topic
- Writes pose messages to CSV with timestamps
- Automatically flushes data to disk

### etl.py
Data pipeline that:
- Reads CSV file with pose data
- Validates and transforms data
- Creates SQLite database
- Loads transformed data into database

## Example

To capture turtle movement data:

1. Terminal 1: Start turtlesim
```bash
ros2 run turtlesim turtlesim_node
```

2. Terminal 2: Start pose logger
```bash
python3 turtle_pose_logger.py
```

3. Terminal 3: Move the turtle (using teleop)
```bash
ros2 run turtlesim turtle_teleop_key
```

4. Terminal 4: Run ETL pipeline (after collecting data)
```bash
python3 etl.py
```

## Output Files

- **turtle_pose.csv**: Raw data with timestamp, position (x, y), orientation (theta), and velocities
- **turtle_data.db**: Processed data ready for analysis and querying

## License

MIT
