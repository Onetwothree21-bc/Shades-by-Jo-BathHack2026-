import videoSurvelance.py as vs

def runSystem():

    #  Run Facial Recognition
    potentialPeople = vs.ImageCheck()
    

    for name,img in potentialPeople:

        # If the face in the image isnt recognised
        if name == "Unknown":
            # Run audio capture:
            audio = RecordAudio()
        
        # If the face is recognised
        else: 
            # Get info from database
            # TODO
            # Print into Colsole logs
            # Send to Bluetooth
            print("add database access here")

            return "data given"

        analyseAudio(audio)
        
        # Add to DataBase here
        print("add funcitonality to add to databases")

        return "New Person"