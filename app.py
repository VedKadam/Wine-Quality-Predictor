from flask import *
import pickle

f = None
try:
	f = open("wine.model", "rb")
	model = pickle.load(f)
except Exception as e:
	print("issue ", e)
finally:
	if f is not None:
		f.close()

app = Flask(__name__)
app.secret_key = "created_by_vedant"

@app.route("/", methods=["GET", "POST"])
def home():
	
	if request.method == "POST":
			try:
				
				fc = request.form["fc"]
				vc = request.form["vc"]
				ca = request.form["ca"]
				rs = request.form["rs"]
				c  = request.form["c"]
				fs = request.form["fs"]
				ts = request.form["ts"]
				den = request.form["den"]
				ph = request.form["ph"]
				s  = request.form["s"]
				alc = request.form["alc"]
				
				d = [[fc, vc, ca, rs, c, fs, ts, den, ph, s, alc]]
				predict = model.predict(d) 
				msg = "Quality of Wine is " + str(predict[0]) + " out of 10"
				return render_template("home.html", msg=msg)
		
			except Exception as e:
				msg = "issue " + str(e)
				return render_template("home.html", msg = msg)
	else:
		return render_template("home.html")

if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)