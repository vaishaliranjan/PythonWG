from flask import Flask, render_template, request,redirect, url_for

#unique flask app name
app= Flask(__name__)
posts={
    0: {
        'post_id':0,
        'title': "Hello, World",
        'content': "This is my first blog."
    }
}


#first url
@app.route("/post/<int:post_id>")
def post(post_id):
    #post=posts[post_id]
    post= posts.get(post_id)
    # return post
    #return render_template("post.html", post)
    if not post:
        return  render_template("404.html",message=f"A post with id {post_id} couldn't be found")
    return render_template("post.html", post= post)
@app.route('/')
def home():
    return render_template("home.jinja2", posts=posts)


# @app.route("/post/form")
# def form():
#     return render_template('create.jinja2')
#
# @app.route("/post/create", methods=["POST"])
# def create():
#     title= request.form.get('title')
#     content= request.form.get('content')
#     post_id= len(posts)
#     posts[post_id]= {
#         'post_id': post_id,
#         'title': title,
#         'content': content
#     }
#     return redirect(url_for("post",post_id=post_id))



@app.route("/post/create", methods=["GET","POST"])
def create():
    if request.method=='POST':
        title= request.form.get('title')
        content= request.form.get('content')
        post_id= len(posts)
        posts[post_id]= {
            'post_id': post_id,
            'title': title,
            'content': content
        }
        return redirect(url_for("post",post_id=post_id))
    return render_template('create.jinja2')

if __name__=="__main__":
    app.run(debug=True)



