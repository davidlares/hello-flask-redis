from flask import Flask, request, render_template
import redis # redis client

# flask instance
app = Flask(__name__)

# default static values in memory
default_key = "1"

# redis init object
cache = redis.StrictRedis(host="redis",port=6379, db=0) # the hostname should be linked to the redis container
cache.set(default_key, "one")

# route handling
@app.route("/", methods=["GET","POST"]) # this handles both verbs
def main():
    key = default_key
    # check if is present on the request
    if "key" in request.form:
        key = request.form["key"]

    # handling post and submit value save
    if request.method == "POST" and request.form["submit"] == "save":
        cache.set(key, request.form["cache_value"]) # adding values

    # set cache_value to None
    cache_value = None
    if cache.get(key): # assigning cache object key value if found
        cache_value = cache.get(key).decode("utf-8") # byte-stream converted into string

    # rendering
    return render_template("index.html", key=key, cache_value=cache_value)

# script initialization
if __name__ == "__main__":
    app.run(host="0.0.0.0") # flask server run script
    # 0.0.0.0 is needed for remote access
