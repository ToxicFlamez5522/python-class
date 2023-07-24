def process_names(name_list):
    print(f"Number of names:{len(name_list)}")

    first_name=[]
    for name in name_list:
        first_name.append(name.split(' ')[0])
    print(f'first names: {first_name}')
    
    
    last_name=[]
    for name in name_list:
        last_name.append(name.split(' ')[1])
    print(f'last names: {last_name}')  

names = ['Jonh Smith', 'Alice Johnson', 'Bob Williams', 'Mary Lee-Smith']

process_names(names)      