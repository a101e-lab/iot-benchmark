# IoT Benchmark Emulator

This script is designed to emulate IoT firmware using Docker containers. It builds and runs a Docker image based on a specified benchmark configuration, and attempts to start a service within the container.

## Prerequisites

- Python 3.x
- Docker

## Installation

1. **Clone the repository:**

   ```bash
   git clone git@github.com:a101e-lab/iot-benchmark.git
   cd iot-benchmark
   ```

2. **Install the required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare your benchmark configuration:**

   Ensure you have a `benchmark.yml` file in your benchmark directory. This file should contain the necessary configuration for building and running the Docker container.

2. **Run the script (use `sudo` if necessary):**

   ```bash
   sudo python3 iot-benchmark/emulation.py -b <path-to-benchmark-directory>
   ```

   Replace `<path-to-benchmark-directory>` with the path to your benchmark directory containing the `benchmark.yml` file.

   **Note:** `sudo` is required because Docker commands may need elevated permissions.

## Troubleshooting

- Ensure Docker is running and accessible from your command line.
- Verify that the `benchmark.yml` file is correctly formatted and contains all necessary fields.
- Check Docker logs for any issues with the container startup.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.
