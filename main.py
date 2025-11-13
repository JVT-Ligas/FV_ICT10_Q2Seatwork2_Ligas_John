from pyscript import document, display

subjects = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE'] # List of subjects
units_subject = (5, 5, 5, 3, 2, 1)  # Units for each subject in order

#General Weighted Average Calculation
def general_weighted_average(e):
    # Get grade values from HTML and convert to float
    science = float(document.getElementById('science').value)
    math = float(document.getElementById('math').value)
    english = float(document.getElementById('english').value)
    ict = float(document.getElementById('ict').value)
    filipino = float(document.getElementById('filipino').value)
    pe = float(document.getElementById('pe').value)
    
    # Get name values from HTML
    Fname = document.getElementById('fname').value
    Lname = document.getElementById('lname').value
    
    # Grades list corresponding to subjects
    grades = [science, math, english, filipino, ict, pe]
    
    # Calculate weighted sum using units for each subject
    weighted_sum = (science * 5 + math * 5 + english * 5 + filipino * 3 + ict * 2 + pe * 1)
    total_units = (5 * 3) + 3 + 2 + 1
    gwa = weighted_sum / total_units


    # Create summary message
    summary = f"""{subjects[0]}: {science:.0f}, 
    {subjects[1]}: {math:.0f},
    {subjects[2]}: {english:.0f},
    {subjects[3]}: {filipino:.0f},
    {subjects[4]}: {ict:.0f},
    {subjects[5]}: {pe:.0f}"""
    # summary of grades formatted to 0 decimal places
    message = f'Your general weighted average is {gwa:.2f}'
    # Display results
    display(f'Name: {Fname} {Lname}', target="student_info")
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output1')