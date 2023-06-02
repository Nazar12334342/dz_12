import asyncio

async def handle_client(reader, writer):
    while True:
        data = await reader.readline()
        if not data:
            break


        num1, num2 = map(int, data.decode().strip().split())


        result_add = await add_numbers(num1, num2)
        result_sub = await subtract_numbers(num1, num2)
        result_mul = await multiply_numbers(num1, num2)


        writer.write(f"Додавання: {result_add}\n".encode())
        writer.write(f"Віднімання: {result_sub}\n".encode())
        writer.write(f"Множення: {result_mul}\n".encode())
        await writer.drain()

    writer.close()

async def add_numbers(num1, num2):

    return num1 + num2

async def subtract_numbers(num1, num2):

    return num1 - num2

async def multiply_numbers(num1, num2):

    return num1 * num2

async def main():
    server = await asyncio.start_server(
        handle_client, 'localhost', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Server started on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
