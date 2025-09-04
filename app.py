from flask import Flask, request, render_template, redirect
app = Flask(__name__)


# Section Home: choose for semester.
@app.route("/", methods=['GET', 'POST'])
def startpage():
    if request.method == 'POST':
        branch = request.form.get("branch")
        semester = request.form.get("semester")
        if semester == "1":
            if branch in ['aids', 'cse', 'it', 'civil', 'ee', 'me']:
                return redirect('/first_year_cs')
                  
        if semester == "3":
            if branch in ['aids', 'cse', 'it']:
                print('aids,cse,it')
                return redirect('/third')
            if branch == 'civil':
                print('civil')
                return redirect('/civil_third_sem')
            if branch == 'ee':
                print('electrical')
                return redirect('/ee_third')
            if branch == 'me':
                print('mechnical')
                return redirect('/me_third')
        
        if semester == "4":
            if branch == 'aids':
                return redirect('/aids_fourth')
            elif branch == 'cse':
                return redirect('/cse_fourth')
            elif branch == 'it':
                return redirect('/it_fourth')
            elif branch == 'civil':
                return redirect('/civil_fourth_sem')
            elif branch == 'ee':
                return redirect('/ee_fourth')
            elif branch == 'me':
                return redirect('/me_fourth')
        
        if semester == "5":
            if branch == 'aids':
                return redirect('/aids_fifth')
            elif branch == 'cse':
                return redirect('/cse_fifth')
            elif branch == 'it':
                return redirect('/it_fifth')
            elif branch == 'civil':
                return redirect('/civil_fifth_sem')
            elif branch == 'ee':
                return redirect('/ee_fifth')
            elif branch == 'me':
                return redirect('/me_fifth')
        
        if semester == "6":            
            if branch == "aids":
                return redirect('/aids_sixth')
            elif branch == 'cse':
                return redirect('/cse_sixth')
            elif branch == 'it':
                return redirect('/it_sixth')
            elif branch == 'civil':
                return redirect('/civil_sixth_sem')
            elif branch == 'ee':
                return redirect('/ee_sixth')
            elif branch == 'me':
                return redirect('/me_sixth')
        
        if semester == "7":
            if branch == "aids":
                return redirect('/aids_seventh')
            elif branch == 'cse':
                return redirect('/cse_seventh')
            elif branch == 'it':
                return redirect('/it_seventh')
            elif branch == 'civil':
                return redirect('/civil_seventh_sem')
            elif branch == 'ee':
                return redirect('/ee_seventh')
            elif branch == 'me':
                return redirect('/me_seventh')
        
        if semester == "8":
            if branch == "aids":
                return redirect('/aids_eighth')
            elif branch == 'cse':
                return redirect('/cse_eighth')
            elif branch == 'it':
                return redirect('/it_eighth')
            elif branch == 'civil':
                return redirect('/civil_eighth_sem')
            elif branch == 'ee':
                return redirect('/ee_eighth')
            elif branch == 'me':
                return redirect('/me_eighth')

    return render_template('home.html')

#Section About
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

#Section Contact
@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')


# ------------------------------------------First Year Calculation--------------------------------------------------------------------------------------------------------------------------
# AIDS/CSE/IT
@app.route("/first_year_cs", methods=['GET', 'POST'])
def second():
    if request.method == 'POST':
        grades = {
            # THEORY SUBJECTS
            "maths1_grade": request.form.get("maths1_grade"),              # Engineering Mathematics-I
            "maths2_grade": request.form.get("maths2_grade"),              # Engineering Mathematics-II
            "chemistry_grade": request.form.get("chemistry_grade"),        # Engineering Chemistry
            "physics_grade": request.form.get("physics_grade"),            # Engineering Physics
            "humanvalues_grade": request.form.get("humanvalues_grade"),    # Human Values
            "commskills_grade": request.form.get("commskills_grade"),      # Communication Skills
            "mech_grade": request.form.get("mech_grade"),                  # Basic Mechanical Engineering
            "progsolving_grade": request.form.get("progsolving_grade"),    # Programming for Problem Solving
            "civil_grade": request.form.get("civil_grade"),                # Basic Civil Engineering
            "electrical_grade": request.form.get("electrical_grade"),      # Basic Electrical Engineering

            # LAB SUBJECTS
            "chemlab_grade": request.form.get("chemlab_grade"),            # Engineering Chemistry Lab
            "physlab_grade": request.form.get("physlab_grade"),            # Engineering Physics Lab
            "hv_activities_grade": request.form.get("hv_activities_grade"),# Human Values Activities
            "langlab_grade": request.form.get("langlab_grade"),            # Language Lab
            "mpworkshop_grade": request.form.get("mpworkshop_grade"),      # Manufacturing Practices Workshop
            "cplab_grade": request.form.get("cplab_grade"),                # Computer Programming Lab
            "civillab_grade": request.form.get("civillab_grade"),          # Basic Civil Engineering Lab
            "electricallab_grade": request.form.get("electricallab_grade"),# Basic Electrical Engineering Lab
            "camd_grade": request.form.get("camd_grade"),                  # Computer Aided Machine Drawing
            "caeg_grade": request.form.get("caeg_grade"),                  # Computer Aided Engineering Graphics

            # SODECA
            "sodeca_grade": request.form.get("sodeca_grade")               # NCC / NSS / Sports (SODECA)
        }
        sgpa = sgpa_cal_first_year(grades)
        return render_template('first_year_cs.html', results=sgpa)
    else:
        return render_template('first_year_cs.html')

def sgpa_cal_first_year(grades):
    grade_point = {
        "na": 0,
        "A++": 10,
        "A+": 9,
        "A": 8.5,
        "B+": 8,
        "B": 7.5,
        "C+": 7,
        "C": 6.5,
        "D+": 6,
        "D": 5.5,
        "E+": 5,
        "E": 4,
        "F": 0,
    }

    total_points_scored = (
        # THEORY SUBJECTS
        grade_point[grades['maths1_grade']] * 4 +
        grade_point[grades['maths2_grade']] * 4 +             # Engineering Mathematics-II
        grade_point[grades['chemistry_grade']] * 4 +          # Engineering Chemistry
        grade_point[grades['physics_grade']] * 4 +            # Engineering Physics
        grade_point[grades['humanvalues_grade']] * 2 +        # Human Values
        grade_point[grades['commskills_grade']] * 2 +         # Communication Skills
        grade_point[grades['mech_grade']] * 2 +               # Basic Mechanical Engineering
        grade_point[grades['progsolving_grade']] * 2 +        # Programming for Problem Solving
        grade_point[grades['civil_grade']] * 2 +              # Basic Civil Engineering
        grade_point[grades['electrical_grade']] * 2 +         # Basic Electrical Engineering

        # LAB SUBJECTS
        grade_point[grades['chemlab_grade']] * 1 +            # Engineering Chemistry Lab
        grade_point[grades['physlab_grade']] * 1 +            # Engineering Physics Lab
        grade_point[grades['hv_activities_grade']] * 1 +      # Human Values Activities
        grade_point[grades['langlab_grade']] * 1 +            # Language Lab
        grade_point[grades['mpworkshop_grade']] * 1.5 +       # Manufacturing Practices Workshop
        grade_point[grades['cplab_grade']] * 1.5 +            # Computer Programming Lab
        grade_point[grades['civillab_grade']] * 1 +           # Basic Civil Engineering Lab
        grade_point[grades['electricallab_grade']] * 1 +      # Basic Electrical Engineering Lab
        grade_point[grades['camd_grade']] * 1.5 +             # Computer Aided Machine Drawing
        grade_point[grades['caeg_grade']] * 1.5 +             # Computer Aided Engineering Graphics

        # SODECA
        grade_point[grades['sodeca_grade']] * 0.5             # SODECA (NCC/NSS/Sports)
    )

    total_credits = 20.5
    sgpa = total_points_scored / total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa >= 10:
        sgpa = 10.00

    return sgpa





# ------------------------------------------3rd semester Calculation--------------------------------------------------------------------------------------------------------------------------
#3rd sem AIDS/CSE/IT
@app.route("/third", methods=['GET', 'POST'])
def third():
    if request.method == 'POST':
        grades = {
            "theory1_grade": request.form.get("theory1_grade"),  # AEM
            "theory2_grade": request.form.get("theory2_grade"),  # TC
            "theory3_grade": request.form.get("theory3_grade"),  # MEFA
            "theory4_grade": request.form.get("theory4_grade"),  # DE
            "theory5_grade": request.form.get("theory5_grade"),  # DSA
            "theory6_grade": request.form.get("theory6_grade"),  # OOP
            "theory7_grade": request.form.get("theory7_grade"),  # SE
            "lab1_grade": request.form.get("lab1_grade"),        # DSA Lab
            "lab2_grade": request.form.get("lab2_grade"),        # OOP Lab
            "lab3_grade": request.form.get("lab3_grade"),        # SE Lab
            "lab4_grade": request.form.get("lab4_grade"),        # DE Lab
            "lab5_grade": request.form.get("lab5_grade"),        # Industrial Training
            "sodeca_grade": request.form.get("sodeca_grade")     # SODECA
        }
        sgpa = sgpa_cal_third(grades)
        return render_template('third.html', results=sgpa)
    else:
        return render_template('third.html')

def sgpa_cal_third(grades):
    grade_point = {
        "na": 0,
        "A++": 10,
        "A+": 9,
        "A": 8.5,
        "B+": 8,
        "B": 7.5,
        "C+": 7,
        "C": 6.5,
        "D+": 6,
        "D": 5.5,
        "E+": 5,
        "E": 4,
        "F": 0,
    }

    total_points_scored = (
        grade_point[grades['theory1_grade']] * 3 +   # Advanced Engineering Mathematics
        grade_point[grades['theory2_grade']] * 2 +   # Technical Communication
        grade_point[grades['theory3_grade']] * 2 +   # MEFA
        grade_point[grades['theory4_grade']] * 3 +   # Digital Electronics
        grade_point[grades['theory5_grade']] * 3 +   # Data Structures and Algorithms
        grade_point[grades['theory6_grade']] * 3 +   # Object Oriented Programming
        grade_point[grades['theory7_grade']] * 3 +   # Software Engineering
        grade_point[grades['lab1_grade']] * 1.5 +    # DS Lab
        grade_point[grades['lab2_grade']] * 1.5 +    # OOPS Lab
        grade_point[grades['lab3_grade']] * 1.5 +    # SE Lab
        grade_point[grades['lab4_grade']] * 1.5 +    # Digital Electronics Lab
        grade_point[grades['lab5_grade']] * 1 +      # Industrial Training
        grade_point[grades['sodeca_grade']] * 0.5    # SODECA
    )

    total_credits = 24.5
    sgpa = total_points_scored / total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa >= 10:
        sgpa = 10.00

    return sgpa


#3rd sem civil
@app.route('/civil_third_sem', methods=['GET', 'POST'])
def civil_third_sem():
    if request.method == "POST":
        grades = {
            # THEORY
            "aem1_grade": request.form.get("aem1_grade"),
            "tc_mefa_grade": request.form.get("tc_mefa_grade"),
            "em_grade": request.form.get("em_grade"),
            "surveying_grade": request.form.get("surveying_grade"),
            "fm_grade": request.form.get("fm_grade"),
            "bmc_grade": request.form.get("bmc_grade"),
            "eg_grade": request.form.get("eg_grade"),

            # PRACTICAL & SESSIONAL
            "surveying_lab_grade": request.form.get("surveying_lab_grade"),
            "fm_lab_grade": request.form.get("fm_lab_grade"),
            "caced_grade": request.form.get("caced_grade"),
            "cem_lab_grade": request.form.get("cem_lab_grade"),
            "geo_lab_grade": request.form.get("geo_lab_grade"),
            "it_grade": request.form.get("it_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }

        sgpa = sgpa_cal_civil_third(grades)   # Calculation function
        return render_template("civil_third.html", results=sgpa)

    return render_template("civil_third.html")

def sgpa_cal_civil_third(grades):
    grade_point = {
        "na": 0,
        "A++": 10,
        "A+": 9,
        "A": 8.5,
        "B+": 8,
        "B": 7.5,
        "C+": 7,
        "C": 6.5,
        "D+": 6,
        "D": 5.5,
        "E+": 5,
        "E": 4,
        "F": 0,
    }

    total_points_scored = (
        # THEORY
        grade_point[grades['aem1_grade']] * 3 +       # Advance Engineering Mathematics - I
        grade_point[grades['tc_mefa_grade']] * 2 +    # Technical Communication / MEFA
        grade_point[grades['em_grade']] * 2 +         # Engineering Mechanics
        grade_point[grades['surveying_grade']] * 3 +  # Surveying
        grade_point[grades['fm_grade']] * 2 +         # Fluid Mechanics
        grade_point[grades['bmc_grade']] * 3 +        # Building Materials and Construction
        grade_point[grades['eg_grade']] * 2 +         # Engineering Geology

        # PRACTICAL & SESSIONAL
        grade_point[grades['surveying_lab_grade']] * 1.5 +   # Surveying Lab
        grade_point[grades['fm_lab_grade']] * 1 +            # Fluid Mechanics Lab
        grade_point[grades['caced_grade']] * 1.5 +           # Computer Aided Civil Engg. Drawing
        grade_point[grades['cem_lab_grade']] * 1 +           # Civil Engg. Materials Lab
        grade_point[grades['geo_lab_grade']] * 1 +           # Geology Lab
        grade_point[grades['it_grade']] * 1 +                # Industrial Training
        grade_point[grades['sodeca_grade']] * 0.5            # SODECA
    )

    total_credits = 24.5
    sgpa = total_points_scored / total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa >= 10:
        sgpa = 10.00

    return sgpa

#3th sem Electrical
@app.route('/ee_third', methods=['GET', 'POST'])
def ee_third():
    if request.method == "POST":
        grades = {
            "maths_grade": request.form.get("maths_grade"),
            "tc_mfa_grade": request.form.get("tc_mfa_grade"),
            "pgp_grade": request.form.get("pgp_grade"),
            "eca_grade": request.form.get("eca_grade"),
            "ae_grade": request.form.get("ae_grade"),
            "em1_grade": request.form.get("em1_grade"),
            "emf_grade": request.form.get("emf_grade"),
            "aelab_grade": request.form.get("aelab_grade"),
            "em1lab_grade": request.form.get("em1lab_grade"),
            "ecdlab_grade": request.form.get("ecdlab_grade"),
            "it_grade": request.form.get("it_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }
        sgpa = sgpa_cal_ee_third(grades)
        return render_template('electrical_third.html', results=sgpa)
    return render_template('electrical_third.html')

def sgpa_cal_ee_third(grades):
    grade_point = {
        "na": 0, "A++": 10, "A+": 9, "A": 8.5,
        "B+": 8, "B": 7.5, "C+": 7, "C": 6.5,
        "D+": 6, "D": 5.5, "E+": 5, "E": 4, "F": 0
    }

    total_points = (
        grade_point[grades['maths_grade']] * 3 +
        grade_point[grades['tc_mfa_grade']] * 2 +
        grade_point[grades['pgp_grade']] * 2 +
        grade_point[grades['eca_grade']] * 3 +
        grade_point[grades['ae_grade']] * 3 +
        grade_point[grades['em1_grade']] * 3 +
        grade_point[grades['emf_grade']] * 2 +
        grade_point[grades['aelab_grade']] * 1 +
        grade_point[grades['em1lab_grade']] * 2 +
        grade_point[grades['ecdlab_grade']] * 2 +
        grade_point[grades['it_grade']] * 1 +
        grade_point[grades['sodeca_grade']] * 0.5
    )

    total_credits = 24.5
    sgpa = total_points / total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa >= 10:
        sgpa = 10.00

    return sgpa


#3rd sem Mechanical
@app.route('/me_third', methods=['GET', 'POST'])
def mech_third_sem():
    if request.method == "POST":
        grades = {
            "maths_grade": request.form.get("maths_grade"),
            "hsmc_grade": request.form.get("hsmc_grade"),
            "mech_grade": request.form.get("mech_grade"),
            "thermo_grade": request.form.get("thermo_grade"),
            "material_grade": request.form.get("material_grade"),
            "solidmech_grade": request.form.get("solidmech_grade"),
            "drawing_grade": request.form.get("drawing_grade"),
            "testinglab_grade": request.form.get("testinglab_grade"),
            "bmechlab_grade": request.form.get("bmechlab_grade"),
            "matlab_grade": request.form.get("matlab_grade"),
            "training_grade": request.form.get("training_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }
        sgpa = sgpa_cal_mech_third_sem(grades)
        return render_template('me_third.html', results=sgpa)
    return render_template('me_third.html')
def sgpa_cal_mech_third_sem(grades):
    grade_point = {
        "na": 0,
        "A++": 10,
        "A+": 9,
        "A": 8.5,
        "B+": 8,
        "B": 7.5,
        "C+": 7,
        "C": 6.5,
        "D+": 6,
        "D": 5.5,
        "E+": 5,
        "E": 4,
        "F": 0
    }
    total_points = (
        grade_point[grades['maths_grade']] * 3 +
        grade_point[grades['hsmc_grade']] * 2 +
        grade_point[grades['mech_grade']] * 2 +
        grade_point[grades['thermo_grade']] * 3 +
        grade_point[grades['material_grade']] * 3 +
        grade_point[grades['solidmech_grade']] * 4 +
        grade_point[grades['drawing_grade']] * 1.5 +
        grade_point[grades['testinglab_grade']] * 1.5 +
        grade_point[grades['bmechlab_grade']] * 1.5 +
        grade_point[grades['matlab_grade']] * 1.5 +
        grade_point[grades['training_grade']] * 1 +
        grade_point[grades['sodeca_grade']] * 0.5
    )
    total_credits = 24.5
    sgpa = total_points / total_credits
    sgpa = float(f"{sgpa:.2f}")
    if sgpa >= 10:
        sgpa = 10.00
    return sgpa





# ------------------------------------------4th semester Calculation--------------------------------------------------------------------------------------------------------------------------
#4th sem CSE
@app.route("/cse_fourth", methods=['GET', 'POST'])
def cse_fourth():
    if request.method == 'POST':
        grades = {
            "theory1_grade": request.form.get("dms_grade"),
            "theory2_grade": request.form.get("mefa_grade"),
            "theory3_grade": request.form.get("tc_grade"),
            "theory4_grade": request.form.get("mp_grade"),
            "theory5_grade": request.form.get("dbms_grade"),
            "theory6_grade": request.form.get("toc_grade"),
            "theory7_grade": request.form.get("dccn_grade"),
            "lab1_grade": request.form.get("mplab_grade"),
            "lab2_grade": request.form.get("dbmslab_grade"),
            "lab3_grade": request.form.get("nplab_grade"),
            "lab4_grade": request.form.get("lsplab_grade"),
            "lab5_grade": request.form.get("javalab_grade"),
            "sodeca_grade": request.form.get("sodeca_grade")
        }
        sgpa = sgpa_cal_fourth(grades)
        return render_template('cse_fourth.html', results=sgpa)
    else:
        return render_template('cse_fourth.html')

#4TH SEM AIDS
@app.route("/aids_fourth", methods=['GET', 'POST'])
def aids_fourth():
    if request.method == 'POST':
        grades = {
            "theory1_grade": request.form.get("dms_grade"),
            "theory2_grade": request.form.get("mefa_grade"),
            "theory3_grade": request.form.get("tc_grade"),
            "theory4_grade": request.form.get("mpi_grade"),
            "theory5_grade": request.form.get("dbms_grade"),
            "theory6_grade": request.form.get("toc_grade"),
            "theory7_grade": request.form.get("dccn_grade"),
            "lab1_grade": request.form.get("mpi_lab_grade"),
            "lab2_grade": request.form.get("dbms_lab_grade"),
            "lab3_grade": request.form.get("np_lab_grade"),
            "lab4_grade": request.form.get("lsp_lab_grade"),
            "lab5_grade": request.form.get("java_lab_grade"),
            "sodeca_grade": request.form.get("sodeca_grade")
        }
        sgpa = sgpa_cal_fourth(grades)
        return render_template('aids_fourth.html', results=sgpa)
    else:
        return render_template('aids_fourth.html')

#4TH SEM IT
@app.route('/it_fourth', methods=['GET','POST'])
def it_fourth():
    if request.method == 'POST':
        grades = {
            "theory1_grade": request.form.get("dms_grade"),
            "theory2_grade": request.form.get("mefa_grade"),
            "theory3_grade": request.form.get("tc_grade"),
            "theory4_grade": request.form.get("poc_grade"),
            "theory5_grade": request.form.get("dbms_grade"),
            "theory6_grade": request.form.get("toc_grade"),
            "theory7_grade": request.form.get("dccn_grade"),
            "lab1_grade": request.form.get("lspl_grade"),
            "lab2_grade": request.form.get("dbmslab_grade"),
            "lab3_grade": request.form.get("nplab_grade"),
            "lab4_grade": request.form.get("javalab_grade"),
            "lab5_grade": request.form.get("wtlab_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }
        sgpa = sgpa_cal_fourth(grades)
        return render_template('it_fourth.html', results=sgpa)
    else:
        return render_template('it_fourth.html') 

def sgpa_cal_fourth(grades):
    grade_point = {
        "na": 0,
        "A++": 10,
        "A+": 9,
        "A": 8.5,
        "B+": 8,
        "B": 7.5,
        "C+": 7,
        "C": 6.5,
        "D+": 6,
        "D": 5.5,
        "E+": 5,
        "E": 4,
        "F": 0,
    }

    total_points_scored = (
        grade_point[grades['theory1_grade']] * 3 +
        grade_point[grades['theory2_grade']] * 2 +
        grade_point[grades['theory3_grade']] * 2 +
        grade_point[grades['theory4_grade']] * 3 +
        grade_point[grades['theory5_grade']] * 3 +
        grade_point[grades['theory6_grade']] * 3 +
        grade_point[grades['theory7_grade']] * 3 +
        grade_point[grades['lab1_grade']] * 1 +
        grade_point[grades['lab2_grade']] * 1.5 +
        grade_point[grades['lab3_grade']] * 1.5 +
        grade_point[grades['lab4_grade']] * 1 +
        grade_point[grades['lab5_grade']] * 1 +
        grade_point[grades['sodeca_grade']] * 0.5
    )

    total_credits = 23.5
    sgpa = total_points_scored / total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa >= 10:
        sgpa = 10.00

    return sgpa

#civil fourth sem
@app.route('/civil_fourth_sem', methods=['GET', 'POST'])
def civil_fourth_sem():
    if request.method == "POST":
        grades = {
            # THEORY
            "aem2_grade": request.form.get("aem2_grade"),
            "mefa_tc_grade": request.form.get("mefa_tc_grade"),
            "becea_grade": request.form.get("becea_grade"),
            "som_grade": request.form.get("som_grade"),
            "he_grade": request.form.get("he_grade"),
            "bp_grade": request.form.get("bp_grade"),
            "ct_grade": request.form.get("ct_grade"),

            # PRACTICAL & SESSIONAL
            "mt_lab_grade": request.form.get("mt_lab_grade"),
            "he_lab_grade": request.form.get("he_lab_grade"),
            "bd_grade": request.form.get("bd_grade"),
            "as_lab_grade": request.form.get("as_lab_grade"),
            "cl_lab_grade": request.form.get("cl_lab_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }

        sgpa = sgpa_cal_civil_fourth(grades)
        return render_template("civil_fourth.html", results=sgpa)

    return render_template("civil_fourth.html")

def sgpa_cal_civil_fourth(grades):
    grade_point = {
        "na": 0,
        "A++": 10,
        "A+": 9,
        "A": 8.5,
        "B+": 8,
        "B": 7.5,
        "C+": 7,
        "C": 6.5,
        "D+": 6,
        "D": 5.5,
        "E+": 5,
        "E": 4,
        "F": 0,
    }

    total_points_scored = (
        # THEORY
        grade_point[grades['aem2_grade']] * 2 +       # AEM-II
        grade_point[grades['mefa_tc_grade']] * 2 +    # MEFA / TC
        grade_point[grades['becea_grade']] * 2 +      # Basic Electronics for Civil Engg. Applications
        grade_point[grades['som_grade']] * 3 +        # Strength of Materials
        grade_point[grades['he_grade']] * 3 +         # Hydraulics Engineering
        grade_point[grades['bp_grade']] * 2 +         # Building Planning
        grade_point[grades['ct_grade']] * 3 +         # Concrete Technology

        # PRACTICAL & SESSIONAL
        grade_point[grades['mt_lab_grade']] * 1 +     # Material Testing Lab
        grade_point[grades['he_lab_grade']] * 1 +     # Hydraulics Engineering Lab
        grade_point[grades['bd_grade']] * 1.5 +       # Building Drawing
        grade_point[grades['as_lab_grade']] * 1 +     # Advanced Surveying Lab
        grade_point[grades['cl_lab_grade']] * 1.5 +   # Concrete Lab
        grade_point[grades['sodeca_grade']] * 0.5     # SODECA
    )

    total_credits = 23.5
    sgpa = total_points_scored / total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa >= 10:
        sgpa = 10.00

    return sgpa

# 4th sem Electrical
@app.route('/ee_fourth', methods=['GET', 'POST'])
def ee_fourth():
    if request.method == "POST":
        grades = {
            "biology_grade": request.form.get("biology_grade"),
            "tc_mefa_grade": request.form.get("tc_mefa_grade"),
            "emi_grade": request.form.get("emi_grade"),
            "em2_grade": request.form.get("em2_grade"),
            "pe_grade": request.form.get("pe_grade"),
            "ss_grade": request.form.get("ss_grade"),
            "de_grade": request.form.get("de_grade"),
            "em2lab_grade": request.form.get("em2lab_grade"),
            "pelab_grade": request.form.get("pelab_grade"),
            "delab_grade": request.form.get("delab_grade"),
            "mlab_grade": request.form.get("mlab_grade"),
            "foundation_grade": request.form.get("foundation_grade"),
        }
        sgpa = sgpa_cal_ee_fourth(grades)
        return render_template('ee_fourth.html', results=sgpa)

    return render_template('ee_fourth.html')
def sgpa_cal_ee_fourth(grades):
    grade_point = {
        "na": 0,
        "A++": 10,
        "A+": 9,
        "A": 8.5,
        "B+": 8,
        "B": 7.5,
        "C+": 7,
        "C": 6.5,
        "D+": 6,
        "D": 5.5,
        "E+": 5,
        "E": 4,
        "F": 0,
    }

    total_points = (
        grade_point[grades['biology_grade']] * 2 +
        grade_point[grades['tc_mefa_grade']] * 2 +
        grade_point[grades['emi_grade']] * 2 +
        grade_point[grades['em2_grade']] * 3 +
        grade_point[grades['pe_grade']] * 3 +
        grade_point[grades['ss_grade']] * 3 +
        grade_point[grades['de_grade']] * 2 +
        grade_point[grades['em2lab_grade']] * 2 +
        grade_point[grades['pelab_grade']] * 2 +
        grade_point[grades['delab_grade']] * 1 +
        grade_point[grades['mlab_grade']] * 1 +
        grade_point[grades['foundation_grade']] * 0.5
    )

    total_credits = 23.5
    sgpa = total_points / total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa >= 10:
        sgpa = 10.00

    return sgpa


#4th semester Mechnical
@app.route('/me_fourth', methods=['GET', 'POST'])
def mech_fourth_sem():
    if request.method == "POST":
        grades = {
            "analytics_grade": request.form.get("analytics_grade"),
            "hsmc_grade": request.form.get("hsmc_grade"),
            "electronics_grade": request.form.get("electronics_grade"),
            "fluidmech_grade": request.form.get("fluidmech_grade"),
            "manufacturing_grade": request.form.get("manufacturing_grade"),
            "machines_grade": request.form.get("machines_grade"),
            "electronics_lab_grade": request.form.get("electronics_lab_grade"),
            "fluidmech_lab_grade": request.form.get("fluidmech_lab_grade"),
            "production_lab_grade": request.form.get("production_lab_grade"),
            "machines_lab_grade": request.form.get("machines_lab_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }
        sgpa = sgpa_cal_mech_fourth_sem(grades)
        return render_template('me_fourth.html', results=sgpa)
    return render_template('me_fourth.html')
def sgpa_cal_mech_fourth_sem(grades):
    grade_point = {
        "na": 0,
        "A++": 10,
        "A+": 9,
        "A": 8.5,
        "B+": 8,
        "B": 7.5,
        "C+": 7,
        "C": 6.5,
        "D+": 6,
        "D": 5.5,
        "E+": 5,
        "E": 4,
        "F": 0
    }
    total_points = (
        grade_point[grades['analytics_grade']] * 2 +
        grade_point[grades['hsmc_grade']] * 2 +
        grade_point[grades['electronics_grade']] * 2 +
        grade_point[grades['fluidmech_grade']] * 4 +
        grade_point[grades['manufacturing_grade']] * 3 +
        grade_point[grades['machines_grade']] * 4 +
        grade_point[grades['electronics_lab_grade']] * 1.5 +
        grade_point[grades['fluidmech_lab_grade']] * 1.5 +
        grade_point[grades['production_lab_grade']] * 1.5 +
        grade_point[grades['machines_lab_grade']] * 1.5 +
        grade_point[grades['sodeca_grade']] * 0.5
    )
    total_credits = 23.5
    sgpa = total_points / total_credits
    sgpa = float(f"{sgpa:.2f}")
    if sgpa >= 10:
        sgpa = 10.00
    return sgpa


# ------------------------------------------5th semester Calculation--------------------------------------------------------------------------------------------------------------------------

# 5th Semester AIDS.
@app.route("/aids_fifth", methods=['GET', 'POST'])
def aids_fifth():
    if request.method == 'POST':
       grades = {
        "dmct_grade": request.form.get("dmct_grade"),
        "cd_grade": request.form.get("cd_grade"),
        "os_grade": request.form.get("os_grade"),
        "cgm_grade": request.form.get("cgm_grade"),
        "aoa_grade": request.form.get("aoa_grade"),
        "fob_grade": request.form.get("fob_grade"),
        "psds_grade": request.form.get("psds_grade"),
        "pds_grade": request.form.get("pds_grade"),
        "cgmlab_grade": request.form.get("cgmlab_grade"),
        "cdlab_grade": request.form.get("cdlab_grade"),
        "aoalab_grade": request.form.get("aoalab_grade"),
        "advjavalab_grade": request.form.get("advjavalab_grade"),
        "it_grade": request.form.get("it_grade"),
        "SODECA": request.form.get("sodeca_grade")        
        }
       sgpa = sgpa_cal_fifth_aids(grades)
       return render_template('aids_fifth.html', results = sgpa)
    else:
        return render_template('aids_fifth.html')
    
def sgpa_cal_fifth_aids(grades):
    #grade_point dictionary
    grade_point = {
        "na":0,
        "A++":10,
        "A+":9,
        "A":8.5,
        "B+":8,
        "B":7.5,
        "C+":7,
        "C":6.5,
        "D+":6,
        "D":5.5,
        "E+":5,
        "E":4,
        "F":0,
    }
    total_points_scored = (grade_point[grades['dmct_grade']]*2)+(grade_point[grades['cd_grade']]*3)+(grade_point[grades['os_grade']]*3)+(grade_point[grades['cgm_grade']]*3)+(grade_point[grades['aoa_grade']]*3)+(grade_point[grades['cgmlab_grade']]*1)+(grade_point[grades['cdlab_grade']]*1)+(grade_point[grades['aoalab_grade']]*1)+(grade_point[grades['advjavalab_grade']]*1)+(grade_point[grades['fob_grade']]*2)+(grade_point[grades['psds_grade']]*2)+(grade_point[grades['pds_grade']]*2)+(grade_point[grades['it_grade']]*2.5)+(grade_point[grades['SODECA']]*0.5)

    total_credits = 23
    sgpa = total_points_scored/total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa>=10 :
        sgpa = 10.00
        
    return sgpa


#5th semester CSE
@app.route("/cse_fifth", methods=['GET', 'POST'])
def cse_fifth():
    if request.method == 'POST':
        grades = {
            "itc_grade": request.form.get("itc_grade"),          # Information Theory & Coding
            "cd_grade": request.form.get("cd_grade"),            # Compiler Design
            "os_grade": request.form.get("os_grade"),            # Operating System
            "cgm_grade": request.form.get("cgm_grade"),          # Computer Graphics & Multimedia
            "aoa_grade": request.form.get("aoa_grade"),          # Analysis of Algorithms
            "wc_grade": request.form.get("wc_grade"),            # Elective - Wireless Communication
            "hci_grade": request.form.get("hci_grade"),          # Elective - Human-Computer Interaction
            "bio_grade": request.form.get("bio_grade"),          # Elective - Bioinformatics
            "cgmlab_grade": request.form.get("cgmlab_grade"),    # CGM Lab
            "cdlab_grade": request.form.get("cdlab_grade"),      # Compiler Design Lab
            "aoalab_grade": request.form.get("aoalab_grade"),    # AOA Lab
            "ajava_grade": request.form.get("ajava_grade"),      # Advance Java Lab
            "it_grade": request.form.get("it_grade"),            # Industrial Training
            "sodeca_grade": request.form.get("sodeca_grade")     # SODECA
        }
        sgpa = sgpa_cal_fifth_cse(grades)
        return render_template('cse_fifth.html', results=sgpa)
    else:
        return render_template('cse_fifth.html')

def sgpa_cal_fifth_cse(grades):
    # Grade point dictionary
    grade_point = {
        "na": 0,
        "A++": 10,
        "A+": 9,
        "A": 8.5,
        "B+": 8,
        "B": 7.5,
        "C+": 7,
        "C": 6.5,
        "D+": 6,
        "D": 5.5,
        "E+": 5,
        "E": 4,
        "F": 0,
    }

    total_points_scored = (
        (grade_point[grades['itc_grade']] * 2) +      # Information Theory & Coding
        (grade_point[grades['cd_grade']] * 3) +       # Compiler Design
        (grade_point[grades['os_grade']] * 3) +       # Operating System
        (grade_point[grades['cgm_grade']] * 3) +      # Computer Graphics & Multimedia
        (grade_point[grades['aoa_grade']] * 3) +      # Analysis of Algorithms
        # Elective - only one will be chosen, rest should be "na"
        (grade_point[grades['wc_grade']] * 2) +
        (grade_point[grades['hci_grade']] * 2) +
        (grade_point[grades['bio_grade']] * 2) +
        (grade_point[grades['cgmlab_grade']] * 1) +   # CGM Lab
        (grade_point[grades['cdlab_grade']] * 1) +    # Compiler Design Lab
        (grade_point[grades['aoalab_grade']] * 1) +   # AOA Lab
        (grade_point[grades['ajava_grade']] * 1) +    # Advance Java Lab
        (grade_point[grades['it_grade']] * 2.5) +     # Industrial Training
        (grade_point[grades['sodeca_grade']] * 0.5)   # SODECA
    )

    total_credits = 23
    sgpa = total_points_scored / total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa >= 10:
        sgpa = 10.00

    return sgpa

#5th semester IT
@app.route("/it_fifth", methods=['GET', 'POST'])
def it_fifth():
    if request.method == 'POST':
        grades = {
            "mpi_grade": request.form.get("mpi_grade"),          # Microprocessor & Interfaces
            "cd_grade": request.form.get("cd_grade"),            # Compiler Design
            "os_grade": request.form.get("os_grade"),            # Operating System
            "cgm_grade": request.form.get("cgm_grade"),          # Computer Graphics & Multimedia
            "aoa_grade": request.form.get("aoa_grade"),          # Analysis of Algorithms
            "wc_grade": request.form.get("wc_grade"),            # Elective - Wireless Communication
            "stpm_grade": request.form.get("stpm_grade"),        # Elective - Software Testing & Project Management
            "bio_grade": request.form.get("bio_grade"),          # Elective - Bioinformatics
            "cgmlab_grade": request.form.get("cgmlab_grade"),    # CGM Lab
            "cdlab_grade": request.form.get("cdlab_grade"),      # Compiler Design Lab
            "aoalab_grade": request.form.get("aoalab_grade"),    # AOA Lab
            "ajava_grade": request.form.get("ajava_grade"),      # Advanced Java Lab
            "it_grade": request.form.get("it_grade"),            # Industrial Training
            "sodeca_grade": request.form.get("sodeca_grade")     # SODECA
        }
        sgpa = sgpa_cal_fifth_it(grades)
        return render_template('it_fifth.html', results=sgpa)
    else:
        return render_template('it_fifth.html')

def sgpa_cal_fifth_it(grades):
    # Grade point dictionary
    grade_point = {
        "na": 0,
        "A++": 10,
        "A+": 9,
        "A": 8.5,
        "B+": 8,
        "B": 7.5,
        "C+": 7,
        "C": 6.5,
        "D+": 6,
        "D": 5.5,
        "E+": 5,
        "E": 4,
        "F": 0,
    }

    total_points_scored = (
        (grade_point[grades['mpi_grade']] * 2) +      # Microprocessor & Interfaces
        (grade_point[grades['cd_grade']] * 3) +       # Compiler Design
        (grade_point[grades['os_grade']] * 3) +       # Operating System
        (grade_point[grades['cgm_grade']] * 3) +      # CGM
        (grade_point[grades['aoa_grade']] * 3) +      # AOA
        # Elective (only one contributes, others should be "na")
        (grade_point[grades['wc_grade']] * 2) +
        (grade_point[grades['stpm_grade']] * 2) +
        (grade_point[grades['bio_grade']] * 2) +
        (grade_point[grades['cgmlab_grade']] * 1) +   # CGM Lab
        (grade_point[grades['cdlab_grade']] * 1) +    # Compiler Lab
        (grade_point[grades['aoalab_grade']] * 1) +   # AOA Lab
        (grade_point[grades['ajava_grade']] * 1) +    # Advanced Java Lab
        (grade_point[grades['it_grade']] * 2.5) +     # Industrial Training
        (grade_point[grades['sodeca_grade']] * 0.5)   # SODECA
    )

    total_credits = 23
    sgpa = total_points_scored / total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa >= 10:
        sgpa = 10.00

    return sgpa

# 5th semester Civil
@app.route('/civil_fifth_sem', methods=['GET', 'POST'])
def civil_fifth_sem():
    if request.method == "POST":
        grades = {
            # THEORY
            "cte_grade": request.form.get("cte_grade"),
            "sa1_grade": request.form.get("sa1_grade"),
            "dcs_grade": request.form.get("dcs_grade"),
            "geo_grade": request.form.get("geo_grade"),
            "wre_grade": request.form.get("wre_grade"),
            "de1_grade": request.form.get("de1_grade"),
            "de2_grade": request.form.get("de2_grade"),

            # PRACTICAL
            "csd_lab_grade": request.form.get("csd_lab_grade"),
            "geo_lab_grade": request.form.get("geo_lab_grade"),
            "wre_lab_grade": request.form.get("wre_lab_grade"),
            "it_grade": request.form.get("it_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }

        sgpa = sgpa_cal_civil_fifth(grades)
        return render_template("civil_fifth.html", results=sgpa)

    return render_template("civil_fifth.html")

def sgpa_cal_civil_fifth(grades):
    grade_point = {
        "na": 0,
        "A++": 10,
        "A+": 9,
        "A": 8.5,
        "B+": 8,
        "B": 7.5,
        "C+": 7,
        "C": 6.5,
        "D+": 6,
        "D": 5.5,
        "E+": 5,
        "E": 4,
        "F": 0,
    }

    total_points_scored = (
        # THEORY
        grade_point[grades['cte_grade']] * 2 +
        grade_point[grades['sa1_grade']] * 2 +
        grade_point[grades['dcs_grade']] * 3 +
        grade_point[grades['geo_grade']] * 3 +
        grade_point[grades['wre_grade']] * 2 +
        grade_point[grades['de1_grade']] * 2 +
        grade_point[grades['de2_grade']] * 2 +

        # PRACTICAL & SESSIONAL
        grade_point[grades['csd_lab_grade']] * 1.5 +
        grade_point[grades['geo_lab_grade']] * 1.5 +
        grade_point[grades['wre_lab_grade']] * 1 +
        grade_point[grades['it_grade']] * 2.5 +
        grade_point[grades['sodeca_grade']] * 0.5
    )

    total_credits = 23
    sgpa = total_points_scored / total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa >= 10:
        sgpa = 10.00

    return sgpa

#5th sem Electrical
@app.route('/ee_fifth', methods=['GET', 'POST'])
def ee_fifth():
    if request.method == "POST":
        grades = {
            "em_grade": request.form.get("em_grade"),
            "ps1_grade": request.form.get("ps1_grade"),
            "cs_grade": request.form.get("cs_grade"),
            "mp_grade": request.form.get("mp_grade"),
            "emd_grade": request.form.get("emd_grade"),
            "pe1_grade": request.form.get("pe1_grade"),
            "ps1lab_grade": request.form.get("ps1lab_grade"),
            "cslab_grade": request.form.get("cslab_grade"),
            "mplab_grade": request.form.get("mplab_grade"),
            "splab_grade": request.form.get("splab_grade"),
            "it_grade": request.form.get("it_grade"),
            "foundation_grade": request.form.get("foundation_grade"),
        }
        sgpa = sgpa_cal_ee_fifth(grades)
        return render_template('ee_fifth.html', results=sgpa)
    return render_template('ee_fifth.html')
def sgpa_cal_ee_fifth(grades):
    grade_point = {
        "na": 0, "A++": 10, "A+": 9, "A": 8.5, "B+": 8,
        "B": 7.5, "C+": 7, "C": 6.5, "D+": 6, "D": 5.5,
        "E+": 5, "E": 4, "F": 0
    }

    total_points = (
        grade_point[grades['em_grade']] * 2 +
        grade_point[grades['ps1_grade']] * 3 +
        grade_point[grades['cs_grade']] * 3 +
        grade_point[grades['mp_grade']] * 3 +
        grade_point[grades['emd_grade']] * 3 +
        grade_point[grades['pe1_grade']] * 2 +
        grade_point[grades['ps1lab_grade']] * 1 +
        grade_point[grades['cslab_grade']] * 1 +
        grade_point[grades['mplab_grade']] * 1 +
        grade_point[grades['splab_grade']] * 1 +
        grade_point[grades['it_grade']] * 2.5 +
        grade_point[grades['foundation_grade']] * 0.5
    )

    total_credits = 23
    sgpa = total_points / total_credits
    sgpa = float(f"{sgpa:.2f}")
    if sgpa >= 10:
        sgpa = 10.00
    return sgpa

#5th sem Mechnical
@app.route('/me_fifth', methods=['GET', 'POST'])
def me_fifth():
    if request.method == "POST":
        grades = {
            "mechatronicsys_grade": request.form.get("mechatronicsys_grade"),
            "ht_grade": request.form.get("ht_grade"),
            "mt_grade": request.form.get("mt_grade"),
            "dme1_grade": request.form.get("dme1_grade"),
            "pom_grade": request.form.get("pom_grade"),
            "pe1_grade": request.form.get("pe1_grade"),
            "mechatroniclab_grade": request.form.get("mechatroniclab_grade"),
            "htlab_grade": request.form.get("htlab_grade"),
            "pelab_grade": request.form.get("pelab_grade"),
            "mdp1_grade": request.form.get("mdp1_grade"),
            "it_grade": request.form.get("it_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }
        sgpa = sgpa_cal_me_fifth(grades)
        return render_template('me_fifth.html', results=sgpa)
    return render_template('me_fifth.html')
def sgpa_cal_me_fifth(grades):
    grade_point = {
        "na": 0, "A++": 10, "A+": 9, "A": 8.5,
        "B+": 8, "B": 7.5, "C+": 7, "C": 6.5,
        "D+": 6, "D": 5.5, "E+": 5, "E": 4, "F": 0
    }

    total_points = (
        grade_point[grades['mechatronicsys_grade']] * 2 +
        grade_point[grades['ht_grade']] * 3 +
        grade_point[grades['mt_grade']] * 3 +
        grade_point[grades['dme1_grade']] * 3 +
        grade_point[grades['pom_grade']] * 2 +
        grade_point[grades['pe1_grade']] * 3 +
        grade_point[grades['mechatroniclab_grade']] * 1 +
        grade_point[grades['htlab_grade']] * 1 +
        grade_point[grades['pelab_grade']] * 1 +
        grade_point[grades['mdp1_grade']] * 1 +
        grade_point[grades['it_grade']] * 2.5 +
        grade_point[grades['sodeca_grade']] * 0.5
    )

    total_credits = 23
    sgpa = total_points / total_credits
    sgpa = float(f"{sgpa:.2f}")
    if sgpa >= 10:
        sgpa = 10.00
    return sgpa








#------------------------------------------------6th Semester------------------------------------------------------------------------------------------
# 6th semester IT.
@app.route("/it_sixth", methods=['GET', 'POST'])
def it_sixth():
    if request.method == 'POST':
        grades = {
            "dip_grade": request.form.get("dip_grade"),
            "ml_grade": request.form.get("ml_grade"),
            "iss_grade": request.form.get("iss_grade"),
            "cao_grade": request.form.get("cao_grade"),
            "ai_grade": request.form.get("ai_grade"),
            "ds_grade": request.form.get("ds_grade"),
            "itc_grade": request.form.get("itc_grade"),
            "cc_grade": request.form.get("cc_grade"),
            "5g_grade": request.form.get("5g_grade"),
            "diplab_grade": request.form.get("diplab_grade"),
            "mllab_grade": request.form.get("mllab_grade"),
            "pylab_grade": request.form.get("pylab_grade"),
            "madlab_grade": request.form.get("madlab_grade"),
            "5glab_grade": request.form.get("5glab_grade"),
            "sodeca_grade": request.form.get("sodeca_grade")
        }
        sgpa = sgpa_cal_sixthsem_IT(grades)
        return render_template('it_sixth.html', results=sgpa)
    else:
        return render_template('it_sixth.html')

def sgpa_cal_sixthsem_IT(grades):
    grade_point = {
        "na":0,
        "A++":10,
        "A+":9,
        "A":8.5,
        "B+":8,
        "B":7.5,
        "C+":7,
        "C":6.5,
        "D+":6,
        "D":5.5,
        "E+":5,
        "E":4,
        "F":0,
    }

    total_points_scored = (
        grade_point[grades['dip_grade']]*2 +
        grade_point[grades['ml_grade']]*3 +
        grade_point[grades['iss_grade']]*2 +
        grade_point[grades['cao_grade']]*3 +
        grade_point[grades['ai_grade']]*2 +
        grade_point[grades['ds_grade']]*3 +
        grade_point[grades['itc_grade']]*2 +
        grade_point[grades['cc_grade']]*2 +
        grade_point[grades['5g_grade']]*2 +
        grade_point[grades['diplab_grade']]*1 +
        grade_point[grades['mllab_grade']]*1.5 +
        grade_point[grades['pylab_grade']]*1.5 +
        grade_point[grades['madlab_grade']]*1 +
        grade_point[grades['5glab_grade']]*1 +
        grade_point[grades['sodeca_grade']]*0.5
    )

    total_credits = 23.5
    sgpa = total_points_scored / total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa > 10:
        sgpa = 10.00

    return sgpa



# 6th semester Calculation for AIDS.
@app.route("/aids_sixth", methods=['GET', 'POST'])
def aids_sixth():
    if request.method == 'POST':
       grades = {
        "dip_grade": request.form.get("dip_grade"),
        "ml_grade": request.form.get("ml_grade"),
        "iss_grade": request.form.get("iss_grade"),
        "cao_grade": request.form.get("cao_grade"),
        "pai_grade": request.form.get("pai_grade"),
        "cc_grade": request.form.get("cc_grade"),

        #Elective Subjects...
        "ann_grade": request.form.get("ann_grade"),
        "nlp_grade": request.form.get("nlp_grade"),
        "nic_grade": request.form.get("nic_grade"),
        
        "diplab_grade": request.form.get("diplab_grade"),
        "mllab_grade": request.form.get("mllab_grade"),
        "pylab_grade": request.form.get("pylab_grade"),
        "madlab_grade": request.form.get("madlab_grade"),
        "sodeca_grade": request.form.get("sodeca_grade")        
        }
       
       sgpa = sgpa_cal_sixthsem_Aids(grades)
       return render_template('aids_sixth.html', results = sgpa)
    else:
        return render_template('aids_sixth.html')

def sgpa_cal_sixthsem_Aids(grades):
    #grade_point dictionary
    grade_point = {
        "na": 0,
        "A++": 10,
        "A+": 9,
        "A": 8.5,
        "B+": 8,
        "B": 7.5,
        "C+": 7,
        "C": 6.5,
        "D+": 6,
        "D": 5.5,
        "E+": 5,
        "E": 4,
        "F": 0,
    }

    total_points_scored = (
        grade_point[grades['dip_grade']] * 2 +
        grade_point[grades['ml_grade']] * 3 +
        grade_point[grades['iss_grade']] * 2 +
        grade_point[grades['cao_grade']] * 3 +
        grade_point[grades['pai_grade']] * 2 +
        grade_point[grades['cc_grade']] * 3 +
        grade_point[grades['ann_grade']] * 2 +
        grade_point[grades['nlp_grade']] * 2 +
        grade_point[grades['nic_grade']]* 2 +
        # Professional elective (take max if multiple filled, else 0)

        # Labs
        grade_point[grades['diplab_grade']] * 1.5 +
        grade_point[grades['mllab_grade']] * 1.5 +
        grade_point[grades['pylab_grade']] * 1.5 +
        grade_point[grades['madlab_grade']] * 1.5 +

        # Sessional
        grade_point[grades['sodeca_grade']] * 0.5
    )

    total_credits = 23.5
    sgpa = total_points_scored/total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa>=10 :
        sgpa = 10.00
        
    return sgpa


# sixth sem cse
@app.route("/cse_sixth", methods=['GET', 'POST'])
def cse_sixth():
    if request.method == 'POST':
        grades = {
            "dip_grade": request.form.get("dip_grade"),             # Digital Image Processing
            "ml_grade": request.form.get("ml_grade"),               # Machine Learning
            "iss_grade": request.form.get("iss_grade"),             # Information Security System
            "cao_grade": request.form.get("cao_grade"),             # Computer Architecture & Org
            "ai_grade": request.form.get("ai_grade"),               # Artificial Intelligence
            "cc_grade": request.form.get("cc_grade"),               # Cloud Computing

            # Professional Electives (separate fieldsets)
            "ds_grade": request.form.get("ds_grade"),               # Distributed System
            "sdn_grade": request.form.get("sdn_grade"),             # Software Defined Network
            "erp_grade": request.form.get("erp_grade"),             # Ecommerce and ERP

            # Practical & Sessional
            "dip_lab_grade": request.form.get("dip_lab_grade"),     # Digital Image Processing Lab
            "ml_lab_grade": request.form.get("ml_lab_grade"),       # Machine Learning Lab
            "python_lab_grade": request.form.get("python_lab_grade"), # Python Lab
            "mad_lab_grade": request.form.get("mad_lab_grade"),     # Mobile App Development Lab
            "soec_grade": request.form.get("soec_grade")            # Social Outreach & Extra Curricular
        }

        sgpa = sgpa_cal_sixthsemcse(grades)
        return render_template('cse_sixth.html', results=sgpa)
    else:
        return render_template('cse_sixth.html')

def sgpa_cal_sixthsemcse(grades):
    # Grade → Point conversion
    grade_point = {
        "na": 0,
        "A++": 10,
        "A+": 9,
        "A": 8.5,
        "B+": 8,
        "B": 7.5,
        "C+": 7,
        "C": 6.5,
        "D+": 6,
        "D": 5.5,
        "E+": 5,
        "E": 4,
        "F": 0,
    }

    # Calculate total points with credits
    total_points_scored = (
        grade_point[grades['dip_grade']] * 2 +
        grade_point[grades['ml_grade']] * 3 +
        grade_point[grades['iss_grade']] * 2 +
        grade_point[grades['cao_grade']] * 3 +
        grade_point[grades['ai_grade']] * 2 +
        grade_point[grades['cc_grade']] * 3 +
        grade_point[grades['ds_grade']] * 2 +
        grade_point[grades['sdn_grade']] * 2 +
        grade_point[grades['erp_grade']]* 2 +
        # Professional elective (take max if multiple filled, else 0)

        # Labs
        grade_point[grades['dip_lab_grade']] * 1.5 +
        grade_point[grades['ml_lab_grade']] * 1.5 +
        grade_point[grades['python_lab_grade']] * 1.5 +
        grade_point[grades['mad_lab_grade']] * 1.5 +

        # Sessional
        grade_point[grades['soec_grade']] * 0.5
    )

    # Total credits
    total_credits = 23.5
    sgpa = total_points_scored / total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa >= 10:
        sgpa = 10.00

    return sgpa


# 6th sem CIVIL
@app.route('/civil_sixth_sem', methods=['GET', 'POST'])
def civil_sixth_sem():
    if request.method == "POST":
        grades = {
            # THEORY
            "wsa_grade": request.form.get("wsa_grade"),
            "sa2_grade": request.form.get("sa2_grade"),
            "ee_grade": request.form.get("ee_grade"),
            "dss_grade": request.form.get("dss_grade"),
            "ec_grade": request.form.get("ec_grade"),
            "dept_elec3_grade": request.form.get("dept_elec3_grade"),
            "dept_elec4_grade": request.form.get("dept_elec4_grade"),

            # PRACTICAL & SESSIONAL
            "eedl_grade": request.form.get("eedl_grade"),
            "ssd_lab_grade": request.form.get("ssd_lab_grade"),
            "qsv_grade": request.form.get("qsv_grade"),
            "wersd_grade": request.form.get("wersd_grade"),
            "fd_grade": request.form.get("fd_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }

        sgpa = sgpa_cal_civil_sixth(grades)
        return render_template("civil_sixth.html", results=sgpa)

    return render_template("civil_sixth.html")

def sgpa_cal_civil_sixth(grades):
    grade_point = {
        "na": 0, "A++": 10, "A+": 9, "A": 8.5,
        "B+": 8, "B": 7.5, "C+": 7, "C": 6.5,
        "D+": 6, "D": 5.5, "E+": 5, "E": 4, "F": 0,
    }

    total_points_scored = (
        # THEORY
        grade_point[grades['wsa_grade']] * 2 +
        grade_point[grades['sa2_grade']] * 3 +
        grade_point[grades['ee_grade']] * 3 +
        grade_point[grades['dss_grade']] * 3 +
        grade_point[grades['ec_grade']] * 2 +
        grade_point[grades['dept_elec3_grade']] * 2 +
        grade_point[grades['dept_elec4_grade']] * 2 +

        # PRACTICAL & SESSIONAL
        grade_point[grades['eedl_grade']] * 1.5 +
        grade_point[grades['ssd_lab_grade']] * 1.5 +
        grade_point[grades['qsv_grade']] * 1 +
        grade_point[grades['wersd_grade']] * 1 +
        grade_point[grades['fd_grade']] * 1 +
        grade_point[grades['sodeca_grade']] * 0.5
    )

    total_credits = 23.5
    sgpa = total_points_scored / total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa >= 10:
        sgpa = 10.00

    return sgpa

#6th sem Electrical
@app.route('/ee_sixth', methods=['GET', 'POST'])
def ee_sixth():
    if request.method == "POST":
        grades = {
            "ca_grade": request.form.get("ca_grade"),
            "ps2_grade": request.form.get("ps2_grade"),
            "psp_grade": request.form.get("psp_grade"),
            "eeca_grade": request.form.get("eeca_grade"),
            "ed_grade": request.form.get("ed_grade"),
            "pe2_grade": request.form.get("pe2_grade"),
            "ps2lab_grade": request.form.get("ps2lab_grade"),
            "edlab_grade": request.form.get("edlab_grade"),
            "psplab_grade": request.form.get("psplab_grade"),
            "mslab_grade": request.form.get("mslab_grade"),
            "foundation_grade": request.form.get("foundation_grade"),
        }
        sgpa = sgpa_cal_ee_sixth(grades)
        return render_template("ee_sixth.html", results=sgpa)
    return render_template("ee_sixth.html")
def sgpa_cal_ee_sixth(grades):
    grade_point = {
        "na": 0,
        "A++": 10,
        "A+": 9,
        "A": 8.5,
        "B+": 8,
        "B": 7.5,
        "C+": 7,
        "C": 6.5,
        "D+": 6,
        "D": 5.5,
        "E+": 5,
        "E": 4,
        "F": 0
    }

    total_points = (
        grade_point[grades['ca_grade']] * 2 +
        grade_point[grades['ps2_grade']] * 3 +
        grade_point[grades['psp_grade']] * 3 +
        grade_point[grades['eeca_grade']] * 3 +
        grade_point[grades['ed_grade']] * 3 +
        grade_point[grades['pe2_grade']] * 3 +
        grade_point[grades['ps2lab_grade']] * 2 +
        grade_point[grades['edlab_grade']] * 2 +
        grade_point[grades['psplab_grade']] * 1 +
        grade_point[grades['mslab_grade']] * 1 +
        grade_point[grades['foundation_grade']] * 0.5
    )

    total_credits = 23.5
    sgpa = total_points / total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa >= 10:
        sgpa = 10.00
    return sgpa

#6th sem Mechnical
@app.route('/me_sixth', methods=['GET', 'POST'])
def me_sixth_sem():
    if request.method == "POST":
        grades = {
            "mm_grade": request.form.get("mm_grade"),
            "cims_grade": request.form.get("cims_grade"),
            "mv_grade": request.form.get("mv_grade"),
            "dme2_grade": request.form.get("dme2_grade"),
            "qm_grade": request.form.get("qm_grade"),
            "pe2_grade": request.form.get("pe2_grade"),
            "cimslab_grade": request.form.get("cimslab_grade"),
            "viblab_grade": request.form.get("viblab_grade"),
            "mdp2_grade": request.form.get("mdp2_grade"),
            "telab_grade": request.form.get("telab_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }
        sgpa = sgpa_cal_me_sixth(grades)
        return render_template('me_sixth.html', results=sgpa)
    return render_template('me_sixth.html')
def sgpa_cal_me_sixth(grades):
    grade_point = {
        "na": 0,
        "A++": 10, "A+": 9, "A": 8.5,
        "B+": 8, "B": 7.5,
        "C+": 7, "C": 6.5,
        "D+": 6, "D": 5.5,
        "E+": 5, "E": 4,
        "F": 0
    }

    total_points = (
        grade_point[grades['mm_grade']] * 2 +
        grade_point[grades['cims_grade']] * 3 +
        grade_point[grades['mv_grade']] * 3 +
        grade_point[grades['dme2_grade']] * 3 +
        grade_point[grades['qm_grade']] * 3 +
        grade_point[grades['pe2_grade']] * 3 +
        grade_point[grades['cimslab_grade']] * 1.5 +
        grade_point[grades['viblab_grade']] * 1.5 +
        grade_point[grades['mdp2_grade']] * 1.5 +
        grade_point[grades['telab_grade']] * 1.5 +
        grade_point[grades['sodeca_grade']] * 0.5
    )

    total_credits = 23.5
    sgpa = total_points / total_credits
    sgpa = float(f"{sgpa:.2f}")
    if sgpa >= 10:
        sgpa = 10.00
    return sgpa

#------------------------------------------------7th Semester------------------------------------------------------------------------------------------

#7th sem Aids
@app.route("/aids_seventh", methods=["GET", "POST"])
def aids_seventh():
    if request.method == "POST":
        grades = {
            "theory_grade": request.form.get("bda_grade"),
            "oe1_grade": request.form.get("oe1_grade"),
            "lab1_grade": request.form.get("bda_lab_grade"),
            "lab2_grade": request.form.get("rplab_grade"),
            "it_grade": request.form.get("it_grade"),
            "seminar_grade": request.form.get("seminar_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }
        sgpa = sgpa_cal_seventh(grades)
        return render_template("aids_seventh.html", results = sgpa)
    return render_template("aids_seventh.html")

#7th sem CSE
@app.route('/cse_seventh', methods=['GET','POST'])
def cse_seventh():
    if request.method == "POST":
        grades = {
            "theory_grade": request.form.get("iot_grade"),
            "oe1_grade": request.form.get("oe_grade"),
            "lab1_grade": request.form.get("iotlab_grade"),
            "lab2_grade": request.form.get("cslab_grade"),
            "it_grade": request.form.get("it_grade"),
            "seminar_grade": request.form.get("seminar_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }
        sgpa = sgpa_cal_seventh(grades)
        return render_template("cse_seventh.html", results = sgpa)
    return render_template("cse_seventh.html")

#7th sem IT
@app.route('/it_seventh', methods=['GET','POST'])
def it_seventh():
    if request.method == "POST":
        grades = {
            "theory_grade": request.form.get("bda_grade"),
            "oe1_grade": request.form.get("oe_grade"),
            "lab1_grade": request.form.get("bdalab_grade"),
            "lab2_grade": request.form.get("cslab_grade"),
            "it_grade": request.form.get("it_grade"),
            "seminar_grade": request.form.get("seminar_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }
        sgpa = sgpa_cal_seventh(grades)
        return render_template("it_seventh.html", results = sgpa)
    return render_template("it_seventh.html")

def sgpa_cal_seventh(grades):
    grade_point = {
        "na": 0,
        "A++": 10,
        "A+": 9,
        "A": 8.5,
        "B+": 8,
        "B": 7.5,
        "C+": 7,
        "C": 6.5,
        "D+": 6,
        "D": 5.5,
        "E+": 5,
        "E": 4,
        "F": 0,
    }

    total_points_scored = (
        grade_point[grades["theory_grade"]] * 3 +
        grade_point[grades["oe1_grade"]] * 3 +
        grade_point[grades["lab1_grade"]] * 2 +
        grade_point[grades["lab2_grade"]] * 2 +
        grade_point[grades["it_grade"]] * 2.5 +
        grade_point[grades["seminar_grade"]] * 2 +
        grade_point[grades["sodeca_grade"]] * 0.5
    )

    total_credits = 15
    sgpa = total_points_scored / total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa >= 10:
        sgpa = 10.00

    return sgpa

# 7th semester CIVIL
@app.route('/civil_seventh_sem', methods=['GET', 'POST'])
def civil_seventh_sem():
    if request.method == "POST":
        grades = {
            # THEORY
            "te_grade": request.form.get("te_grade"),
            "oe1_grade": request.form.get("oe1_grade"),

            # PRACTICAL & SESSIONAL
            "rm_lab_grade": request.form.get("rm_lab_grade"),
            "pp_lab_grade": request.form.get("pp_lab_grade"),
            "ss_lab_grade": request.form.get("ss_lab_grade"),
            "emd_lab_grade": request.form.get("emd_lab_grade"),
            "pt_grade": request.form.get("pt_grade"),
            "seminar_grade": request.form.get("seminar_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }

        sgpa = sgpa_cal_civil_seventh(grades)
        return render_template("civil_seventh.html", results=sgpa)

    return render_template("civil_seventh.html")

def sgpa_cal_civil_seventh(grades):
    grade_point = {
        "na": 0,
        "A++": 10,
        "A+": 9,
        "A": 8.5,
        "B+": 8,
        "B": 7.5,
        "C+": 7,
        "C": 6.5,
        "D+": 6,
        "D": 5.5,
        "E+": 5,
        "E": 4,
        "F": 0,
    }

    total_points_scored = (
        # THEORY
        grade_point[grades['te_grade']] * 3 +      # Transportation Engineering
        grade_point[grades['oe1_grade']] * 3 +     # Open Elective-I

        # PRACTICAL & SESSIONAL
        grade_point[grades['rm_lab_grade']] * 1 +   # Road Material Testing Lab
        grade_point[grades['pp_lab_grade']] * 1 +   # Professional Practices Lab
        grade_point[grades['ss_lab_grade']] * 1 +   # Soft Skills Lab
        grade_point[grades['emd_lab_grade']] * 1 +  # Env. Monitoring & Design Lab
        grade_point[grades['pt_grade']] * 2.5 +     # Practical Training
        grade_point[grades['seminar_grade']] * 2 +  # Seminar
        grade_point[grades['sodeca_grade']] * 0.5   # SODECA
    )

    total_credits = 15
    sgpa = total_points_scored / total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa >= 10:
        sgpa = 10.00

    return sgpa

#7th sem Electrical
@app.route('/ee_seventh', methods=['GET', 'POST'])
def ee_seventh():
    if request.method == "POST":
        grades = {
            "wse_grade": request.form.get("wse_grade"),
            "pqf_grade": request.form.get("pqf_grade"),
            "csd_grade": request.form.get("csd_grade"),
            "oe1_grade": request.form.get("oe1_grade"),
            "eslab_grade": request.form.get("eslab_grade"),
            "acslab_grade": request.form.get("acslab_grade"),
            "it_grade": request.form.get("it_grade"),
            "seminar_grade": request.form.get("seminar_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }
        sgpa = sgpa_cal_ee_seventh(grades)
        return render_template("ee_seventh.html", results=sgpa)
    return render_template("ee_seventh.html")
def sgpa_cal_ee_seventh(grades):
    grade_point = {
        "na": 0,
        "A++": 10,
        "A+": 9,
        "A": 8.5,
        "B+": 8,
        "B": 7.5,
        "C+": 7,
        "C": 6.5,
        "D+": 6,
        "D": 5.5,
        "E+": 5,
        "E": 4,
        "F": 0
    }

    total_points = (
        grade_point[grades['wse_grade']] * 3 +
        grade_point[grades['pqf_grade']] * 3 +
        grade_point[grades['csd_grade']] * 3 +
        grade_point[grades['oe1_grade']] * 3 +
        grade_point[grades['eslab_grade']] * 2 +
        grade_point[grades['acslab_grade']] * 2 +
        grade_point[grades['it_grade']] * 2.5 +
        grade_point[grades['seminar_grade']] * 2 +
        grade_point[grades['sodeca_grade']] * 0.5
    )

    total_credits = 15
    sgpa = total_points / total_credits
    sgpa = float(f"{sgpa:.2f}")
    if sgpa >= 10:
        sgpa = 10.00
    return sgpa

#7th sem Mechnical
@app.route('/me_seventh', methods=['GET', 'POST'])
def me_seventh():
    if request.method == "POST":
        grades = {
            "iceng_grade": request.form.get("iceng_grade"),
            "or_grade": request.form.get("or_grade"),
            "turbo_grade": request.form.get("turbo_grade"),
            "oe1_grade": request.form.get("oe1_grade"),
            "fea_grade": request.form.get("fea_grade"),
            "thermal_lab_grade": request.form.get("thermal_lab_grade"),
            "qc_lab_grade": request.form.get("qc_lab_grade"),
            "it_grade": request.form.get("it_grade"),
            "seminar_grade": request.form.get("seminar_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }
        sgpa = sgpa_cal_me_seventh(grades)
        return render_template('me_seventh.html', results=sgpa)
    return render_template('me_seventh.html')
def sgpa_cal_me_seventh(grades):
    grade_point = {
        "na": 0, "A++": 10, "A+": 9, "A": 8.5,
        "B+": 8, "B": 7.5, "C+": 7, "C": 6.5,
        "D+": 6, "D": 5.5, "E+": 5, "E": 4, "F": 0
    }

    total_points = (
        grade_point[grades['iceng_grade']] * 3 +
        grade_point[grades['or_grade']] * 3 +
        grade_point[grades['turbo_grade']] * 3 +
        grade_point[grades['oe1_grade']] * 3 +
        grade_point[grades['fea_grade']] * 1.5 +
        grade_point[grades['thermal_lab_grade']] * 1.5 +
        grade_point[grades['qc_lab_grade']] * 1 +
        grade_point[grades['it_grade']] * 2.5 +
        grade_point[grades['seminar_grade']] * 2 +
        grade_point[grades['sodeca_grade']] * 0.5
    )

    total_credits = 15
    sgpa = total_points / total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa > 10:
        sgpa = 10.00
    return sgpa


#------------------------------------------------8th Semester------------------------------------------------------------------------------------------
#8th sem cse
@app.route('/aids_eighth', methods=['GET', 'POST'])
def aids_eighth():
    if request.method == "POST":
        grades = {
            "theory_grade": request.form.get("dla_grade"),
            "oe2_grade": request.form.get("oe2_grade"),
            "lab1_grade": request.form.get("dlalab_grade"),
            "lab2_grade": request.form.get("rplab_grade"),
            "project_grade": request.form.get("project_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }
        sgpa = sgpa_cal_eighth_sem(grades)
        return render_template('aids_eighth.html', results = sgpa)
    return render_template('aids_eighth.html')

#8th sem CSE
@app.route('/cse_eighth', methods=['GET', 'POST'])
def cse_eighth():
    if request.method == "POST":
        grades = {
            "theory_grade": request.form.get("bda_grade"),
            "oe2_grade": request.form.get("oe2_grade"),
            "lab1_grade": request.form.get("bdalab_grade"),
            "lab2_grade": request.form.get("stvlab_grade"),
            "project_grade": request.form.get("project_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }
        sgpa = sgpa_cal_eighth_sem(grades)
        return render_template('cse_eighth.html', results = sgpa)
    return render_template('cse_eighth.html')

#8th sem IT
@app.route('/it_eighth', methods=['GET', 'POST'])
def it_eighth():
    if request.method == "POST":
        grades = {
            "theory_grade": request.form.get("iot_grade"),
            "oe2_grade": request.form.get("oe2_grade"),
            "lab1_grade": request.form.get("iotlab_grade"),
            "lab2_grade": request.form.get("stvlab_grade"),
            "project_grade": request.form.get("project_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }
        sgpa = sgpa_cal_eighth_sem(grades)
        return render_template('it_eighth.html', results = sgpa)
    return render_template('it_eighth.html')

def  sgpa_cal_eighth_sem(grades):
    grade_point = {
        "na": 0, "A++": 10, "A+": 9, "A": 8.5,
        "B+": 8, "B": 7.5, "C+": 7, "C": 6.5,
        "D+": 6, "D": 5.5, "E+": 5, "E": 4, "F": 0
    }

    total_points = (
        grade_point[grades['theory_grade']] * 3 +
        grade_point[grades['oe2_grade']] * 3 +
        grade_point[grades['lab1_grade']] * 1 +
        grade_point[grades['lab2_grade']] * 1 +
        grade_point[grades['project_grade']] *  7+
        grade_point[grades['sodeca_grade']] * 0.5
    )

    total_credits = 15.5
    sgpa = total_points / total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa >= 10:
        sgpa = 10.00

    return sgpa


# 8th semester CIVIL
@app.route('/civil_eighth_sem', methods=['GET', 'POST'])
def civil_eighth_sem():
    if request.method == "POST":
        grades = {
            # THEORY
            "ppcm_grade": request.form.get("ppcm_grade"),
            "oe2_grade": request.form.get("oe2_grade"),

            # PRACTICAL & SESSIONAL
            "ppcm_lab_grade": request.form.get("ppcm_lab_grade"),
            "pavement_design_grade": request.form.get("pavement_design_grade"),
            "project_grade": request.form.get("project_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }

        sgpa = sgpa_cal_civil_eighth(grades)
        return render_template("civil_eighth.html", results=sgpa)

    return render_template("civil_eighth.html")

def sgpa_cal_civil_eighth(grades):
    grade_point = {
        "na": 0,
        "A++": 10,
        "A+": 9,
        "A": 8.5,
        "B+": 8,
        "B": 7.5,
        "C+": 7,
        "C": 6.5,
        "D+": 6,
        "D": 5.5,
        "E+": 5,
        "E": 4,
        "F": 0,
    }

    total_points_scored = (
        # THEORY
        grade_point[grades['ppcm_grade']] * 3 +         # Project Planning & Construction Management
        grade_point[grades['oe2_grade']] * 3 +          # Open Elective-II

        # PRACTICAL & SESSIONAL
        grade_point[grades['ppcm_lab_grade']] * 1 +     # Project Planning & Construction Mgmt Lab
        grade_point[grades['pavement_design_grade']] * 1 +  # Pavement Design
        grade_point[grades['project_grade']] * 7 +      # Project
        grade_point[grades['sodeca_grade']] * 0.5       # SODECA
    )

    total_credits = 15.5
    sgpa = total_points_scored / total_credits
    sgpa = float(f"{sgpa:.2f}")

    if sgpa > 10:
        sgpa = 10.00

    return sgpa

#8th sem Electrical
@app.route('/ee_eighth', methods=['GET', 'POST'])
def ee_eighth():
    if request.method == "POST":
        grades = {
            "hvdc_grade": request.form.get("hvdc_grade"),
            "rectifier_grade": request.form.get("rectifier_grade"),
            "drives_grade": request.form.get("drives_grade"),
            "oe2_grade": request.form.get("oe2_grade"),
            "energylab_grade": request.form.get("energylab_grade"),
            "project_grade": request.form.get("project_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }
        sgpa = sgpa_cal_ee_eighth(grades)
        return render_template("ee_eighth.html", results=sgpa)
    return render_template("ee_eighth.html")
def sgpa_cal_ee_eighth(grades):
    grade_point = {
        "na": 0,
        "A++": 10, "A+": 9, "A": 8.5,
        "B+": 8, "B": 7.5,
        "C+": 7, "C": 6.5,
        "D+": 6, "D": 5.5,
        "E+": 5, "E": 4,
        "F": 0
    }

    total_points = (
        grade_point[grades['hvdc_grade']] * 3 +
        grade_point[grades['rectifier_grade']] * 3 +
        grade_point[grades['drives_grade']] * 3 +
        grade_point[grades['oe2_grade']] * 3 +
        grade_point[grades['energylab_grade']] * 2 +
        grade_point[grades['project_grade']] * 7 +
        grade_point[grades['sodeca_grade']] * 0.5
    )

    total_credits = 15.5
    sgpa = total_points / total_credits
    sgpa = float(f"{sgpa:.2f}")
    if sgpa >= 10:
        sgpa = 10.00
    return sgpa

#8th sem Mechnical
@app.route('/me_eighth', methods=['GET', 'POST'])
def me_eighth():
    if request.method == "POST":
        grades = {
            "hev_grade": request.form.get("hev_grade"),
            "som_grade": request.form.get("som_grade"),
            "am_grade": request.form.get("am_grade"),
            "oe2_grade": request.form.get("oe2_grade"),
            "ie_lab_grade": request.form.get("ie_lab_grade"),
            "metrology_lab_grade": request.form.get("metrology_lab_grade"),
            "project_grade": request.form.get("project_grade"),
            "sodeca_grade": request.form.get("sodeca_grade"),
        }
        sgpa = sgpa_cal_me_eighth(grades)
        return render_template('me_eighth.html', results=sgpa)
    return render_template('me_eighth.html')
def sgpa_cal_me_eighth(grades):
    grade_point = {
        "na": 0,
        "A++": 10,
        "A+": 9,
        "A": 8.5,
        "B+": 8,
        "B": 7.5,
        "C+": 7,
        "C": 6.5,
        "D+": 6,
        "D": 5.5,
        "E+": 5,
        "E": 4,
        "F": 0
    }

    total_points = (
        grade_point[grades['hev_grade']] * 3 +
        grade_point[grades['som_grade']] * 3 +
        grade_point[grades['am_grade']] * 3 +
        grade_point[grades['oe2_grade']] * 3 +
        grade_point[grades['ie_lab_grade']] * 1 +
        grade_point[grades['metrology_lab_grade']] * 1 +
        grade_point[grades['project_grade']] * 7 +
        grade_point[grades['sodeca_grade']] * 0.5
    )

    total_credits = 15.5
    sgpa = total_points / total_credits
    sgpa = float(f"{sgpa:.2f}")
    if sgpa > 10:
        sgpa = 10.00
    return sgpa

if __name__ == '__main__':
    app.run(debug = True)