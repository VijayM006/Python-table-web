from flask import Flask,render_template
vj=Flask(__name__)
@vj.route("/")
def table():
    Student_list = [{"Name":"Sivapackia","Age":22 ,"Roll_No": 101, "Marks":[90,75,80,98,65]},
                    {"Name":"Siva","Age":21 ,"Roll_No": 102, "Marks":[90,75,80,78,99]},
                    {"Name":"Vilobin","Age":21 ,"Roll_No": 103, "Marks":[94,75,80,88,35]},
                    {"Name":"Mahadevi","Age":27 ,"Roll_No": 104, "Marks":[70,85,80,98,35]},          
                    {"Name":"Nisha","Age":23 ,"Roll_No": 105, "Marks":[90,75,85,98,35]},
                    {"Name":"Vaisali","Age":27 ,"Roll_No": 106, "Marks":[80,98,35,90,75]},
                    {"Name":"Vijay","Age":22 ,"Roll_No": 107, "Marks":[90,80,98,35,75]},
                    {"Name":"Mohamed Ismail","Age":22 ,"Roll_No": 108, "Marks":[75,80,90,98,35]}
                    ]
    
    return render_template("index.html",student=Student_list)
if __name__=="__main__":
    vj.run(debug=True)
