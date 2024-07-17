from flask import Flask, render_template, request
import utlis

app = Flask(__name__)

@app.route('/')
def home():
    categories = utlis.load_category()
    return render_template('index.html', categories=categories)

@app.route('/products')
def product_list():
    cate_id = request.args.get('category_id')
    kw = request.args.get('keyword')
    from_price = request.args.get('from_price')
    to_price = request.args.get('to_price')
    products = utlis.load_product(cate_id=cate_id,
                                  kw=kw,
                                  from_price=from_price,
                                  to_price=to_price)
    return render_template('product.html', products=products)

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product_detail = utlis.get_product_by_id(product_id)
    return render_template('product_detail.html', product_detail=product_detail)
      
if __name__ == '__main__':
    app.run(debug=True)
