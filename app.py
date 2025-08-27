from flask import Flask, request, render_template, redirect
app = Flask(__name__)


# Section Home: choose for semester.
@app.route("/", methods=['GET', 'POST'])
def startpage():
    if request.method == 'POST':
        branch = request.form.get("branch")
        semester = request.form.get("semester")
        if semester == "1":
            if branch == 'aids'or'cse'or'it':
                return redirect('/first_year_cs')
        if semester == "2":
            if branch == 'aids'or'cse'or'it':
                return redirect('/first_year_cs')
        if semester == "3":
            if branch == 'aids'or'cse'or'it':
                return redirect('/third')
        if semester == "4":
            if branch == 'aids':
                return redirect('/aids_fourth')
            elif branch == 'cse':
                return redirect('/cse_fourth')
            elif branch == 'it':
                return redirect('/it_fourth')
        if semester == "5":
            if branch == 'aids':
                return redirect('/aids_fifth')
            elif branch == 'cse':
                return redirect('/cse_fifth')
            elif branch == 'it':
                return redirect('/it_fifth')
        if semester == "6":            
            if branch == "aids":
                return redirect('/aids_sixth')
            elif branch == 'cse':
                return redirect('/cse_sixth')
            elif branch == 'it':
                return redirect('/it_sixth')
        if semester == "7":
            if branch == "aids":
                return redirect('/aids_seventh')
            elif branch == 'cse':
                return redirect('/cse_seventh')
            elif branch == 'it':
                return redirect('/it_seventh')
        if semester == "8":
            if branch == "aids":
                return redirect('/aids_eighth')
            elif branch == 'cse':
                return redirect('/cse_eighth')
            elif branch == 'it':
                return redirect('/it_eighth')

    return render_template('home.html')

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























































if __name__ == '__main__':
    app.run(debug = True)