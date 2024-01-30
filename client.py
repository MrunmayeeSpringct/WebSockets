import asyncio
import json
import websockets

async def hello():
    # Read the configuration data from the .json file
    with open('config.json', 'r') as json_file:
        config = json.load(json_file)

    # Connect to the WebSocket server using the port number from the config file
    async with websockets.connect("ws://localhost:{}".format(config["port"])) as websocket:
        print("Connected to the server")
        await websocket.send("Hello world!")
        message = await websocket.recv()
        print(f"Received: {message}")
        while True:
            user_input = input("Press q to quit: ")
            if user_input == "q":
                break
        print("Disconnected from the server")

asyncio.run(hello())
