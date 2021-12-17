from backend.core.config import HOST, PORT
import uvicorn


if __name__ == '__main__':
    uvicorn.run('backend:app', host=HOST, port=PORT, debug=True, reload=True)
