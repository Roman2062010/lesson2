marks = [
    {'school_class': '1a', 'scores': [4,4,3,5,2]},
    {'school_class': '2a', 'scores': [3,4,5,5,5]},
    {'school_class': '3a', 'scores': [5,5,4,5,3]},
    {'school_class': '4a', 'scores': [3,5,5,5,5]},
    {'school_class': '5a', 'scores': [3,4,4,4,4]}
]

y = 0

for school_class in marks:
    x = sum(school_class['scores']) / len(marks)
    classes_count = len(marks)

    print(x)
    
    y += x

print(y/classes_count)
    
   
    
   

    

