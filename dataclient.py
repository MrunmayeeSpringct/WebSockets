import asyncio
import websockets
import json

async def handle_connection():
    with open('config.json', 'r') as file:
        config = json.load(file)

    port = int(config['port'])
    uri = f'ws://localhost:{port}'

    while True:
        try:
            async with websockets.connect(uri) as websocket:
                print("Connected to server")

                while True:
                    # Send a request to the server for data
                    request = input("Enter your request: ")
                    await websocket.send(request)
                    print(f"Request sent to server: {request}")

                    # Receive the response from the server
                    response = await websocket.recv()
                    print(f"Received response from server: {response}")

                    # Prompt the user to make another request or quit
                    choice = input("Enter 'r' to make another request or 'q' to quit: ")
                    if choice.lower() == 'q':
                        exit()

        except websockets.exceptions.ConnectionClosedError:
            print("Server disconnected. Trying to reconnect...")
            await asyncio.sleep(5)  # Wait for 5 seconds before attempting to reconnect

async def main():
    while True:
        try:
            await handle_connection()
        except Exception as e:
             print("Trying to reconnect...")
             await asyncio.sleep(5)  # Wait for 5 seconds before attempting to reconnect

asyncio.run(main())

