from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def instant():
    html_content = """
    <html>
      <head>
        <title>Production Output</title>
        <style>
          body { font-family: Arial, sans-serif; background-color: #f0f0f0; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
          .container { background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
          h1 { color: #333; }
        </style>
      </head>
      <body>
        <div class="container">
          <h1>Live from production!</h1>
        </div>
      </body>
    </html>
    """
    return HTMLResponse(content=html_content)