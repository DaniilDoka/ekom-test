from dotenv import dotenv_values

config = {
   **dotenv_values('app/.env')
}

if not config:
   raise RuntimeError('empty config')
