# Pepper Teleoperation Interface (Naoqi 2.5)

This project provides a teleoperation interface for controlling an older Pepper robot running **Naoqi 2.5**. The application allows the robot to execute movement, speech, and predefined behaviors via keyboard input. The `main.py` script connects to the robot over a network and uses Naoqi's services to perform various tasks.

## Features

- **Movement Control**: Use keyboard inputs to move Pepper forward, backward, and rotate left or right.
- **Speech Control**: Make Pepper speak predefined phrases or custom sentences in both Italian and English.
- **Gesture Control**: Trigger gestures like a handshake, hug, and various other behaviors.
- **Volume Control**: Set Pepper's volume to 60% by default.
- **Autonomous Abilities**: Enable or disable autonomous abilities like Basic Awareness and blinking.

## Requirements

- A Pepper robot running **Naoqi 2.5** (Linux-based).
- A PC connected to the same network as the Pepper robot.
- Python 2.7 installed on the PC.
- A `sentences.txt` file with custom phrases.
- Naoqi Python SDK installed on your local machine.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/pepper-teleoperation-interface-naoqi-2.5.git
   cd pepper-teleoperation-interface-naoqi-2.5
   ```
   
2. Prepare Required Files:
    * Ensure that you have a sentences.txt file in the same directory. This file should contain the phrases that the robot will speak, one per line.
    * Optionally, prepare files pepper_sentences_it.txt and pepper_sentences_en.txt for additional predefined sentences in Italian and English.

3. Install Dependencies:
    * Make sure you have the Naoqi Python SDK installed. You can find the SDK here.
    * Install other dependencies if necessary:
	    ```bash
	    pip install qi
	    ```
   
## Usage

1. Run the Application:
    * To start the teleoperation interface, execute the script, providing the robot’s IP address and port (usually 9559):
	    ```bash
	    python teleoperation.py --ip <ROBOT_IP> --port 9559
	    ```

3. Control Pepper via Keyboard Input:
When the program starts, it will ask you to select a language (Italian or English). You can then control the robot with the following keyboard inputs.

Movement commands:
* Move Forward: w
* Move Backward: x
* Rotate Left: a
* Rotate Right: d
* Stop Movement: s
* Increase Speed: e
* Decrease Speed: c

Speech commands:
* Pressing Enter will make Pepper say the next sentence from the sentences.txt file.
* Numbers 1 to 19 trigger predefined sentences.
* Custom phrases can be spoken by typing the sentence.

Gesture Commands:
* 2: Trigger a hug gesture.
* 3: Trigger a handshake gesture.
* n: Perform a “Namaste” gesture.
* h: Perform a greeting.
* k: Perform a “Konnichiwa” gesture.

4. Autonomous Life Management:
   * The script disables Listening Movement and Speaking Movement but leaves Basic Awareness and other abilities enabled. These can be further customized as needed.

## Troubleshooting
   * Connection Issues: If the robot does not connect, verify that the IP address and port are correct. Use --ip <ROBOT_IP> and --port 9559 in the command.
   * Naoqi SDK Issues: Ensure that the Naoqi SDK is installed correctly and is accessible via the Python environment.
   * Permission Issues: Your robot's movement commands or behaviors might be restricted. Check that the robot has the proper permissions and is in a state to accept commands (e.g., not on standby).

## License

This project is licensed under the **GNU General Public License (GPL)**. Please take a look at the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, feel free to reach out:
  * GitHub: [lucregrassi](https://github.com/lucregrassi)
  * Email: lucrezia.grassi@edu.unige.it


