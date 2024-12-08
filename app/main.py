import uvicorn
from fastapi import FastAPI
from app.config import config
from app.routes import router

app = FastAPI()
app.include_router(router)

if __name__ == '__main__':
    print("""
⢸⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⡷⠀⠀
⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀
⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇ Are ya winning son?
⢸⠀⠀⠀⠀⠀⠖⠒⠒⠒⢤⠀⠀⠀⡇
⢸⠀⠀⣀⢤⣼⣀⡠⠤⠤⠼⠤⡄⠀⡇⠀
⢸⠀⠀⠑⡤⠤⡒⠒⠒⡊⠙⡏⠀⢀⡇⠀
⢸⠀⠀⠀⠇⠀⣀⣀⣀⣀⢀⠧⠟⠁⡇
⢸⠀⠀⠀⠸⣀⠀⠀⠈⢉⠟⠓⠀⠀⡇
⢸⠀⠀⠀⠀⠈⢱⡖⠋⠁⠀⠀⠀⠀⡇
⢸⠀⠀⠀⠀⣠⢺⠧⢄⣀⠀⠀⣀⣀⡇
⢸⠀⠀⠀⣠⠃⢸⠀⠀⠈⠉⡽⠿⠯⡆
⢸⠀⠀⣰⠁⠀⢸⠀⠀⠀⠀⠉⠉⠉⡇
⢸⠀⠀⠣⠀⠀⢸⢄⠀⠀⠀⠀⠀⠀⡇
⢸⠀⠀⠀⠀⠀⢸⠀⢇⠀⠀⠀⠀⠀⡇
""")
    uvicorn.run(app, host='0.0.0.0', port=int(config['SERVER_PORT']))
