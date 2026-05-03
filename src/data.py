import csv, json, hashlib
#CSV to dictionary function
def csv_to_dictionary(file_path):
    try:
        with open(file_path, mode = 'r'):
            pass
    except FileNotFoundError:
        print('An error was encountered! Invalid file path.')
        return {'error': FileNotFoundError}
    except Exception as e:
        print(f"An unexpected error was encountered: {e}. ")
        return {'error': e}
    #create empty list
    finished = []
    #open csv file in read mode
    with open(file_path, mode = 'r') as file:
        #create csv reader
        reader = csv.reader(file)
        #get first line in reader
        header = next(reader)
        #loop through reader:
        for line in reader:
            #create empty dictionary
            current_line = {}
            #set iterator to 0
            i = 0
            #loop through first line:
            for column in header:
                #create new line in the dictionary with the first line value as the key and the respective line value as the value
                current_line[column] = line[i]
                i += 1
            #add dictionary to list
            finished.append(current_line)
        return finished

#save dictionary to csv function
def save_csv(dic,save_to):
    try:
        with open(save_to, mode = 'r'):
            pass
    except FileNotFoundError:
        print('An error was encountered! Invalid file path.')
        return {'error': FileNotFoundError}
    except Exception as e:
        print(f"An unexpected error was encountered: {e}. ")
        return {'error': e}
    #get header info
    header = dic[0].keys()
    #open file
    with open(save_to,'w',newline='') as file:
        #create dict writer object
        writer = csv.DictWriter(file,header)
        #write header
        writer.writeheader()
        #write all rows
        writer.writerows(dic)

#JSON writer function
def json_dump(file_path,items):
    #if input is not a dictionary:
    if not type(items) is dict:
        #return false
        return False
    #if file path does not exist
    try:
        with open(file_path,'r'):
            pass
    except FileNotFoundError:
        create_json(file_path)
    except Exception:
        #return false
        return False
    #dictify the dictionary
    items = dictify(items)
    #open given file path
    with open(file_path,'w') as file:
        #write dictionary to it
        json.dump(items, file)
    #return true
    return True

#dictify function
def dictify(items):
    if type(items) is list:
        dictified = []
        #loop through given dictionary or list
        for item in items:
            #if current item is a list or dictionary
            if type(item) is dict or type(item) is list:
                #dictify it (recursion!)
                item = dictify(item)
            #if current item is an instance of one of our classes
            elif hasattr(item,'__dict__'):
                #run __dict__ on it to get it in dictionary form and set a variable to that
                #add a new key to the dictionary "classtype" and set it equal to typeof object
                classtype = type(item).__name__
                item = item.__dict__
                item['classtype'] = classtype
                #replace the object in the dictionary with the __dict__ified object
            dictified.append(item)
        return dictified
    elif type(items) is dict:
        dictified = {}
        for itemkey in items.keys():
            item = items[itemkey]
            if type(item) is dict or type(item) is list:
                item = dictify(item)
            elif hasattr(item,'__dict__'):
                classtype = type(item).__name__
                item = item.__dict__
                item['classtype'] = classtype
            dictified[itemkey] = item
        return dictified
    #return the dictionary


#undictify function
def undictify(items):
    #loop through given dictionary or list
    if type(items) is list:
        undictified = []
        for item in items:
            #if current item is a list or dictionary
            if type(item) is dict or type(item) is list:
                #undictify it (recursion!)
                item = undictify(item)
            #if current item is a dictionary with the "classtype" key
            try:
                item['classtype']
                obj = True
            except:
                obj = False
            if obj:
                try:
                    classtype = globals()[item['classtype']]
                    item.pop('classtype')
                    #create an object with the properties specified in the dictionary
                    itemobj = classtype()
                    for key in item.keys():
                        value = item[key]
                        setattr(itemobj,key,value)
                    item = itemobj
                except KeyError:
                    print(f'The class {item['classtype']} is not imported into helper.py! Import it at the top of helper.py to make loading work properly!')
                except Exception as e:
                    print(f'Unknown error when loading object! {e}')
            #replace the dictionary in the parent dictionary/list with th new object
            undictified.append(item)
    elif type(items) is dict:
        undictified = {}
        for itemkey in items.keys():
            item = items[itemkey]
            #if current item is a list or dictionary
            if type(item) is dict or type(item) is list:
                #undictify it (recursion!)
                item = undictify(item)
            #if current item is a dictionary with the "classtype" key
            try:
                item['classtype']
                obj = True
            except:
                obj = False
            if obj:
                try:
                    classtype = globals()[item['classtype']]
                    item.pop('classtype')
                    #create an object with the properties specified in the dictionary
                    itemobj = classtype()
                    for key in item.keys():
                        value = item[key]
                        setattr(itemobj,key,value)
                    item = itemobj
                except KeyError:
                    print(f'The class {item['classtype']} is not imported into helper.py! Import it at the top of helper.py to make loading work properly!')
                except Exception as e:
                    print(f'Unknown error when loading object! {e}')
            #replace the dictionary in the parent dictionary/list with th new object
            undictified[itemkey] = item
    #return the dictionary
    return undictified

def create_json(file_path):
    try:
        with open(file_path,'w') as file:
            file.write('{}')
    except:
        print('Directory does not exist!')

#JSON reader function
def json_pull(file_path):
    #if file path does not exist
    try:
        with open(file_path,'r'):
            pass
    except:
        #return false
        return False
    #open file path
    with open(file_path,'r') as file:
        #grab data as a dictionary
        data = json.load(file)
        #undictify it
        data = undictify(data)
    #return data
    return data

def encrypt(value):
    hasher = hashlib.sha256()
    encoded = value.encode('utf_8')
    hasher.update(encoded)
    return hasher.hexdigest()