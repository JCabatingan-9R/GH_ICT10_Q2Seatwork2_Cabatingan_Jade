from pyscript import display, document


def gwacalc(e):
    # remove repeat
    document.querySelector("#about").innerText = ""
    document.querySelector("#ave").innerText = ""
    document.querySelector("#h2").innerText = ""

    # get name of student
    fname = document.getElementById('fname').value
    lname = document.getElementById('lname').value
    name = fname + ' ' + lname # combine to get fullname of student

    # use float() for calculations
    sci_ = float(document.getElementById('sci').value)
    eng_ = float(document.getElementById('eng').value)
    ict_ = float(document.getElementById('ict').value)
    math_ = float(document.getElementById('math').value)
    fil_ = float(document.getElementById('fil').value)
    pe_ = float(document.getElementById('pe').value)
    
    # list with subjects
    subjects = ['SCIENCE', 'ENGLISH', 'ICT', 'MATH', 'FILIPINO', 'PHYSICAL EDUCATION']
    
    #tuple with subjects with numerical value
    grades = (sci_, eng_, ict_, math_, fil_, pe_)

    # tuple with subect units
    subjunits= (5, 5, 2, 5, 3, 1)

    # multiplying grade to number of units
    sci_calc = grades[0] * subjunits[0]
    eng_calc = grades[1] * subjunits[1]
    ict_calc = grades[2] * subjunits[2]
    math_calc = grades[3] * subjunits[3]
    fil_calc = grades[4] * subjunits[4]
    pe_calc = grades[5] * subjunits[5]

    # adds total grades
    final_calc = sci_calc + eng_calc + ict_calc + math_calc + fil_calc + pe_calc

    # adds total units
    subjunits_total = subjunits[0] + subjunits[1] + subjunits[2] + subjunits[3] + subjunits[4] + subjunits[5]

    # gets the average
    average = final_calc / subjunits_total

    # multisting for grade information
    multi = f"""
    {subjects[0]}: {sci_:.2f}
    {subjects[1]}: {eng_:.2f}
    {subjects[2]}: {ict_:.2f}
    {subjects[3]}: {math_:.2f}
    {subjects[4]}: {fil_:.2f}
    {subjects[5]}: {pe_:.2f}
    """

    display(name, target='h2')
    display(multi, target='about')
    display(f'Your General Weighted Average is {average:.2f}', target='ave')

    if average > 75: # if statement for passing grade
        display(f'Congratulations, you have passed!', target='ave')
    else: # else statement for failing grade
        display(f'Oh no...You've failed!', target='ave')
