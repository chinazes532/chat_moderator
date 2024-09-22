import aiosqlite as sq


async def create_db():
    print('Creating database...')

    async with sq.connect('database.db') as conn:
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                warn_count INTEGER
            )
        ''')
        await conn.commit()


async def insert_user(user_id, warn_count):
    async with sq.connect('database.db') as conn:
        await conn.execute('''
            INSERT INTO users (user_id, warn_count) VALUES (?, ?)
        ''', (user_id, warn_count))
        await conn.commit()


async def get_user(user_id):
    async with sq.connect('database.db') as conn:
        async with conn.execute('SELECT * FROM users WHERE user_id = ?', (user_id,)) as cursor:
            return await cursor.fetchone()


async def add_warn(user_id):
    async with sq.connect('database.db') as conn:
        await conn.execute('''
            UPDATE users SET warn_count = warn_count + 1 WHERE user_id = ?
        ''', (user_id,))
        await conn.commit()


async def delete_all_warn(user_id):
    async with sq.connect('database.db') as conn:
        await conn.execute('''
            UPDATE users SET warn_count = 0 WHERE user_id = ?
        ''', (user_id,))
        await conn.commit()

