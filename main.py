from pyscript import display, document

def general_weighted_average(e):    
    # These gets the values entered from input feilds
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value
    sci = float(document.getElementById('sci').value)
    math = float(document.getElementById('math').value)
    eng = float(document.getElementById('eng').value)
    fil = float(document.getElementById('fil').value)
    ict = float(document.getElementById('ict').value)
    pe = float(document.getElementById('pe').value)

    subjects = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE']
#                   0         1         2          3        4      5
#   calculates for average and its weights
    weighted_sum = (sci * 5 + math * 5 + eng * 5 + fil * 3 + ict * 2 + pe * 1)
    total_units = (5 * 3) + 3 + 2 + 1
    gwa = weighted_sum / total_units

#this is encharge of displaying the entered values of the grades
    summary = f"""{subjects[0]}: {sci:.0f}
{subjects[1]}: {math:.0f}
{subjects[2]}: {eng:.0f}
{subjects[3]}: {fil:.0f}
{subjects[4]}: {ict:.0f}
{subjects[5]}: {pe:.0f}
    """
#combines everything together to make message
    display(f'Name: {first_name} {last_name}', target="student_info")
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')
