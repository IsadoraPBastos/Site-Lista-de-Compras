from flask import Flask, render_template, request

app = Flask(__name__)

itenscompra = []
lista_calculo = []



@app.route("/")
def principal():
    return render_template("index.html")
    

@app.route("/lista_compra", methods=["POST","GET"])
def lista_compra():
    if request.method == "POST":
        if request.form.get("item"):
            itenscompra.append(request.form.get("item"))
        
    return render_template("lista_compra.html", itenscompra=itenscompra)

@app.route("/limpar_lista1", methods=["POST"])
def limpar_lista1():
    global itenscompra
    itenscompra = []
    return render_template("lista_compra.html")


@app.route("/calcular_despesa", methods=["POST","GET"])
def calcular_despesa():
    if request.method=="POST":
        item = request.form.get("item")
        preco = request.form.get("preco")
        qtde = request.form.get("qtde")
        if (item and preco and qtde):
            lista_calculo.append({"item":item, "preco":preco, "qtde":qtde, "preco_total":(float(preco)*float(qtde))})
    return render_template("calcular_despesa.html", lista_calculo=lista_calculo)

@app.route("/limpar_lista", methods=["POST"])
def limpar_lista():
    global lista_calculo
    lista_calculo = []
    return render_template("calcular_despesa.html")

if __name__=="__main__":
    app.run(debug=True)