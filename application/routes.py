from application import app 
from flask import render_template, request, redirect, url_for
from application.forms import NewDish 
import sqlite3

@app.route("/")
def Hello():
    return render_template ("base.html")

@app.route("/new_dish", methods=['GET', 'POST'])
def add_new_dish():
    
    form = NewDish(request.form)

    if request.method == "GET":
        return render_template ("add_dish.html", form = form)
    
    else:
        if form.validate():
            print("He validado")
            
            list_ingredients = []
            valing = ""

            for i in range (1,5): 
                valing= "ingredient"+str(i)
                print("soy type valing", type(valing))
                print("I am valinfg", valing)
                Ing = request.values.get(valing)
                if Ing not in list_ingredients and Ing != None: 
                    list_ingredients.append (Ing)
            
            str1 = ''.join(list_ingredients)
            print (str1, "Lista de ingredientes")
            
            conn = sqlite3.connect("application/data/dishes_data.db")
            cur = conn.cursor()
            query = "INSERT INTO dishes (Name, Ingredients) values (?, ?);"
            datos = (request.values.get('name_dish'), str1)
            try:
                cur.execute(query, datos)
                conn.commit()
            except Exception as e:
                print("INSERT - Error en acceso a base de datos: {}".format(e))
                conn.close()
                return "ERROR base de datos"

            conn.close()

            return redirect(url_for("Hello"))
        else:
            return render_template ("add_dish.html", form = form)

        
     