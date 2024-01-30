import asyncio
import json
import websockets

async def echo(websocket, path):
    print(f"Client connected: {websocket.remote_address}")
    try:
        async for message in websocket:
            await websocket.send(message)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        print(f"Client disconnected: {websocket.remote_address}")

async def main():
    # Prompt the user for the port number
    port = int(input("Enter the port number: "))

    # Create a dictionary with the configuration data
    config_data = {
        "port": port
    }

    # Write the configuration data to a .json file
    with open('config.json', 'w') as json_file:
        json.dump(config_data, json_file, indent=4)

    # Start the WebSocket server using the port number from the config file
    async with websockets.serve(echo, "localhost", port):
        print(f"Server started on port {port}")
        await asyncio.Future()

asyncio.run(main())
