from flask import Flask

app=Flask(__name__)

@app.route("/")
def test():
    return ("CONGRATULATIONS. If you can see this page, it means that you have completed it successfully.")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=80)
   
    