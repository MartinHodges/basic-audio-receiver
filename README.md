# basic-audio-receiver
A python application that provides a server that receives POSTed .wav files and saves them to a file for further processing. This works with the [api-audio-stream project](https://github.com/MartinHodges/rpi-audio-stream).

## Features

- Receives `.wav` files through HTTP POST requests.
- Saves incoming audio files to a configurable directory.
- Simple REST API for integration with other audio streaming or processing tools.
- Easy to deploy and run on Raspberry Pi or other Linux/macOS systems.

## Usage

1. **Install dependencies**  
Run the following command to install required Python packages:
```sh
pip install -r requirements.txt
```

2. **Start the server (on Mac)**  
```
python3 server.py
```

3. **Access saved files**  
Uploaded files are saved in the configured directory (see `server.py` for details).

## Configuration

- Default port: `3030`
- Default upload directory: `uploads/`
- You can modify these settings in `server.py`.

## Requirements

- Python 3.7+
- Flask (or another web framework, see `requirements.txt`)

## License

MIT License

## Author

Martin
